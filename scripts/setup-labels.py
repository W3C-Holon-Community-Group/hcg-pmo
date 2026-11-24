#!/usr/bin/env python3
"""Create or update the HCG labels in one or more repos from .github/labels.json.

Safe to re-run: existing labels are updated in place, labels listed with
"rename_from" are renamed (so they stay on their issues), and nothing is deleted.
GitHub's other default labels (bug, question, ...) are left alone.

Needs the GitHub CLI (`gh`), logged in as someone with write access to each repo.

Usage:
  python3 scripts/setup-labels.py --dry-run
  python3 scripts/setup-labels.py
  python3 scripts/setup-labels.py OWNER/REPO [OWNER/REPO ...]
"""
import argparse
import json
import pathlib
import subprocess
import sys
import urllib.parse

DEFAULT_REPOS = [
    "W3C-Holon-Community-Group/working-groups",
    "W3C-Holon-Community-Group/hcg-pmo",
]
LABELS_FILE = pathlib.Path(__file__).resolve().parent.parent / ".github" / "labels.json"


def gh(*args, input_obj=None):
    cmd = ["gh", "api", *args]
    data = json.dumps(input_obj) if input_obj is not None else None
    if data is not None:
        cmd += ["--input", "-"]
    res = subprocess.run(cmd, input=data, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd)}\n{res.stderr.strip() or res.stdout.strip()}")
    return json.loads(res.stdout) if res.stdout.strip() else None


def existing_labels(repo):
    pages = gh("--paginate", "--slurp", f"repos/{repo}/labels?per_page=100")
    return {lbl["name"].lower(): lbl for page in pages for lbl in page}


def sync(repo, wanted, dry_run):
    print(f"\n== {repo}")
    have = existing_labels(repo)
    for lbl in wanted:
        body = {"new_name": lbl["name"], "color": lbl["color"], "description": lbl["description"]}
        current = have.get(lbl["name"].lower())
        old = lbl.get("rename_from")
        if current is None and old and old.lower() in have:
            action, target = f"rename '{have[old.lower()]['name']}' ->", have[old.lower()]["name"]
        elif current is not None:
            same = (current["color"].lower() == lbl["color"].lower()
                    and (current.get("description") or "") == lbl["description"]
                    and current["name"] == lbl["name"])
            if same:
                print(f"  ok      {lbl['name']}")
                continue
            action, target = "update", current["name"]
        else:
            action, target = "create", None

        print(f"  {action:7} {lbl['name']}")
        if dry_run:
            continue
        if target is None:
            gh("-X", "POST", f"repos/{repo}/labels",
               input_obj={"name": lbl["name"], "color": lbl["color"], "description": lbl["description"]})
        else:
            gh("-X", "PATCH", f"repos/{repo}/labels/{urllib.parse.quote(target, safe='')}", input_obj=body)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("repos", nargs="*", default=DEFAULT_REPOS, help="OWNER/REPO (default: working repo and hcg-pmo)")
    ap.add_argument("--dry-run", action="store_true", help="show what would change, change nothing")
    args = ap.parse_args()

    wanted = json.loads(LABELS_FILE.read_text())["labels"]
    failed = False
    for repo in args.repos:
        try:
            sync(repo, wanted, args.dry_run)
        except RuntimeError as err:
            failed = True
            print(f"  ERROR: {err}", file=sys.stderr)
    if args.dry_run:
        print("\nDry run: nothing was changed.")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
