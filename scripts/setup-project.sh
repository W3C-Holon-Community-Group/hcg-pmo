#!/usr/bin/env bash
# Create the custom fields on the HCG org Project. See project/FIELDS.md for the
# full spec, including the manual steps (Status options, workflows, views).
#
# Needs: gh CLI logged in with the "project" scope:  gh auth refresh -s project
# Usage: scripts/setup-project.sh <project-number> [org]
#        DRY_RUN=1 scripts/setup-project.sh <project-number>
set -euo pipefail

NUMBER="${1:?usage: $0 <project-number> [org]}"
ORG="${2:-W3C-Holon-Community-Group}"

run() {
  if [[ "${DRY_RUN:-0}" == "1" ]]; then printf 'would run:'; printf ' %q' "$@"; echo; else "$@"; fi
}

existing="$(gh project field-list "$NUMBER" --owner "$ORG" --format json --jq '.fields[].name' 2>/dev/null || true)"

create_field() {
  local name="$1"; shift
  if grep -qxF "$name" <<<"$existing"; then
    echo "ok      $name (already exists; check its options against project/FIELDS.md)"
  else
    echo "create  $name"
    run gh project field-create "$NUMBER" --owner "$ORG" --name "$name" "$@"
  fi
}

create_field "Team" --data-type SINGLE_SELECT \
  --single-select-options "Core Specification,Databook,Harmonization,Identity,Industry Utilization,Network Architecture,Messaging and Serialization,Shared,PMO"
create_field "Quarter goal" --data-type SINGLE_SELECT --single-select-options "Unplanned"
create_field "Target date"  --data-type DATE
create_field "Source"       --data-type SINGLE_SELECT --single-select-options "Meeting,Drive,Issue,Agent"

cat <<'EOF'

Fields done. Now finish by hand (project/FIELDS.md):
  2. Status options: Inbox, Ready, In progress, In review, Done, Parked
  3. Built-in workflows
  4. Views
  5. Link both repos, run the test issue
EOF
