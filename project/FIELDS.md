# HCG Project board: field and view spec

One **org-level GitHub Project** ("HCG") pulls issues and PRs from the working repo and `hcg-pmo`. Contributors see one board; each team sees only its slice.

Setup is partly scripted ([`scripts/setup-project.sh`](../scripts/setup-project.sh) creates the custom fields) and partly manual, because GitHub doesn't let scripts create views or turn on built-in workflows. The manual steps are listed below in order.

## 1. Create the Project

Org page → **Projects → New project → Board**. Name it **HCG**, and set visibility to **Public** so non-members can follow along. Note the project number from its URL (`.../projects/<number>`).

## 2. Fields

| Field | Type | Values | Set by |
|---|---|---|---|
| **Status** | Single select (built-in) | `Inbox`, `Ready`, `In progress`, `In review`, `Done`, `Parked` | Built-in workflows and Actions (below); people may move cards by hand |
| **Team** | Single select | `Core Specification`, `Databook`, `Harmonization`, `Identity`, `Industry Utilization`, `Network Architecture`, `Shared`, `PMO` | PMO at triage (later: the inbox-triage automation, mirroring the `team:` label) |
| **Quarter goal** | Single select | One option per current quarterly goal, named like its milestone, e.g. `2027-Q1 Core spec draft 1`. Starts with `Unplanned`. | PMO at quarterly planning |
| **Target date** | Date | Optional | Whoever owns the item |
| **Source** | Single select | `Meeting`, `Drive`, `Issue`, `Agent` | The person or agent opening the item; notes intake sets `Meeting` |

Also show these built-in fields: **Assignees**, **Labels**, **Repository**, **Milestone**, **Linked pull requests**.

**Status options:** the built-in Status field starts with `Todo`, `In Progress`, `Done`. Edit it in **Settings → Fields → Status** to the six values above, in that order. Rename `Todo` to `Inbox` rather than deleting it, so the default workflows keep pointing at it.

**Why both Quarter goal and Milestone:** milestones belong to one repo, but a goal usually spans both. The Quarter goal field is the cross-repo grouping; create a milestone of the same name in each repo that carries work for the goal. At the end of the quarter, rename the option `… (closed)` rather than deleting it, so history stays grouped.

## 3. Built-in workflows

**Settings → Workflows.** Turn on:

| Workflow | Setting |
|---|---|
| Auto-add to project | One per repo (working repo, `hcg-pmo`); filter `is:issue,pr is:open` |
| Item added to project | Status → `Inbox` |
| Item reopened | Status → `Ready` |
| Pull request linked to issue | Status → `In review` |
| Pull request merged | Status → `Done` |
| Item closed | Status → `Done` |
| Auto-archive items | `is:closed updated:<@today-90d` |

Two moves need GitHub Actions, built in a later step: **a `team:` label moves Inbox → Ready**, and **the 45-day stale rule moves In progress → Ready**.

## 4. Views

Create each view with **New view**, then save the filter and layout.

| View | Layout | Filter | Group / sort | For |
|---|---|---|---|---|
| **All work** | Board, columns by Status | `-status:Done` (show Done only if useful) | — | Everyone |
| **Core Specification** | Board | `label:"team:core-spec"` | — | Team lead walk-through |
| **Databook** | Board | `label:"team:data-book"` | — | ″ |
| **Harmonization** | Board | `label:"team:harmonization"` | — | ″ |
| **Identity** | Board | `label:"team:identity"` | — | ″ |
| **Industry Utilization** | Board | `label:"team:industry"` | — | ″ |
| **Network Architecture** | Board | `label:"team:network-arch"` | — | ″ |
| **Shared** | Board | `label:"team:shared"` | — | Cross-team use cases |
| **PMO triage** | Table | `status:Inbox` | Sort by created, oldest first | Weekly PMO triage |
| **Decisions pending** | Table | `label:"type:decision" is:open` | Sort by Target date | Monthly meeting, leadership |
| **Help wanted** | Table | `label:"good-first-issue","help-wanted" status:Ready` | Group by Team | Newcomers |
| **Roadmap** | Roadmap | `-"quarter goal":Unplanned` | Group by Quarter goal; dates from Target date | Quarterly planning |

Team views filter on the **label**, not the Team field, so they work before triage automation fills the field.

## 5. Link repos and check

1. **Settings → Manage access**: give the org's members *Write*, PMO admins *Admin*.
2. In each repo, **Projects → Link a project → HCG**, so the board shows on the repo's Projects tab.
3. Open a test issue in each repo. It should appear in **Inbox**. Add `team:pmo`, close it, and confirm it reaches **Done**.
