# One-time setup

Do these in order. Each step is safe to repeat.

## 1. Repo settings

`W3C-Holon-Community-Group/hcg-pmo` exists. In its **Settings**:

- **General → Features:** Issues on; Discussions off for now (it is still a proposal); Wiki off.
- **Collaborators and teams:** Christine and Kurt Cagle *Admin*, Patrick Audley *Maintain*, Heather Ray *Admin*.
- **Branches → Add rule for `main`:** require a pull request with 1 approval; no force pushes.

## 2. Labels, in both repos

```bash
python3 scripts/setup-labels.py --dry-run   # look first
python3 scripts/setup-labels.py
```

This creates or updates the labels in [`.github/labels.json`](../.github/labels.json) in the working repo and `hcg-pmo`, and renames GitHub's `good first issue` and `help wanted` to the HCG names so nothing is duplicated. It deletes nothing.

## 3. Issue forms in the working repo

The four forms live in this repo's [`.github/ISSUE_TEMPLATE/`](../.github/ISSUE_TEMPLATE/). Tasks, use cases and meeting notes mostly come in through the working repo, so copy the same folder there in a PR:

```bash
cp -r .github/ISSUE_TEMPLATE ../working-groups/.github/
```

Keep the two copies identical: change them here first, then copy.

## 4. Project board

Create the org Project by hand (step 1 of [`project/FIELDS.md`](../project/FIELDS.md)), then:

```bash
gh auth refresh -s project
DRY_RUN=1 scripts/setup-project.sh <project-number>
scripts/setup-project.sh <project-number>
```

Finish the manual steps in `project/FIELDS.md`: Status options, built-in workflows, views, and the test issue.
