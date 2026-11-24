# Automation registry

Every HCG automation is listed here. If it isn't in this registry, it isn't a group automation: it's somebody's prototype.

## The rule

An automation is a group asset only when it ships with **all five pieces**:

| Piece | Where | Why |
|---|---|---|
| Skill | `automation/skills/<name>/SKILL.md` | Step-by-step instructions any agent that reads skills can follow, plus helper scripts |
| Prompts | `automation/prompts/<name>.md` | Plain Markdown anyone can paste into the AI tool they use |
| Runbook | `automation/runbooks/<name>.md` | How to run it by hand, tell it broke, fix it, switch it off and hand it over |
| Workflow | `.github/workflows/<name>.yml` | The scheduled or event-driven version, running in GitHub Actions |
| Registry entry | This file | Name, purpose, trigger, owner, backup owner, secrets, links |

A piece that genuinely doesn't apply (a one-off with no workflow, an Action with no AI step and so no prompt) is marked `n/a` with a reason, never left blank.

It also has to:

- **Run on group infrastructure:** GitHub Actions in the HCG org, not a scheduled task on someone's personal account.
- **Use group-owned credentials:** org secrets issued to the HCG bot account or an org-owned GitHub App, never a personal token.
- **Have two people:** an owner and a backup owner, both able to run it from the runbook alone.
- **Have a manual path:** the runbook says how to do the job without the automation, so an outage never blocks the group.

Once a quarter, someone other than the author runs one automation from its runbook alone and fixes the docs where they got stuck. Record it in the *Last handover test* column.

## Registry

Status: `planned` → `building` → `live` → `retired`.

| Name | Purpose | Trigger | Status | Owner | Backup | Secrets | Skill | Prompts | Runbook | Workflow | Last handover test |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `notes-opener` | Opens a "Notes: Team, date" issue the day before each meeting; pings the team lead if no notes arrive within 48 h | Schedule (daily) | planned | Christine Connors | Kurt Cagle | `GITHUB_TOKEN` | n/a (no AI step) | n/a (no AI step) | — | — | — |
| `stale-nudges` | Nudge at 30 days without activity; back to Ready and unassigned at 45 | Schedule (daily) | planned | Christine Connors | Kurt Cagle | `GITHUB_TOKEN` | n/a (no AI step) | n/a (no AI step) | — | — | — |
| `notes-intake` | Turns meeting-bot output into a notes PR in the right `meetings/` folder, with drafted issues and decisions | `repository_dispatch` from the webhook relay | planned | Christine Connors | Kurt Cagle | Relay signing secret, AI API key, HCG GitHub App | — | — | — | — | — |
| `weekly-digest` | Summarizes board activity; posts to GitHub and the mailing list | Schedule (weekly) | planned | Christine Connors | Kurt Cagle | AI API key, HCG GitHub App, list-posting credential | — | — | — | — | — |
| `inbox-triage` | Suggests team label, type and duplicates for new issues | `issues: opened` | planned | Christine Connors | Kurt Cagle | AI API key | — | — | — | — | — |
| `drive-migration` | One-off: inventories Drive and converts or archives each file | Manual | planned | Christine Connors | Kurt Cagle | Drive access (TBD) | — | — | — | n/a (one-off) | — |
| `promote-to-w3c` | Opens a PR on `w3c-cg/holon` for `ready-to-promote` items; labels the source `promoted` on merge | `issues: labeled` | planned | Christine Connors | Kurt Cagle | HCG GitHub App with access to `w3c-cg/holon` | n/a (no AI step) | n/a (no AI step) | — | — | — |

Owners above are defaults until each automation is built; reassign when you build one.

## Adding an automation

1. Open a **Task** issue in this repo labelled `team:pmo`.
2. Add a row here with status `building`.
3. Add the five pieces in one PR, starting from [`runbooks/_template.md`](runbooks/_template.md).
4. A maintainer (Patrick Audley) reviews; the backup owner confirms they can follow the runbook.
5. Set status to `live` once it has run successfully on group infrastructure.
