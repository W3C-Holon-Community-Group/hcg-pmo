# HCG PMO

The Program Management Office for the W3C Holon Community Group (HCG): a means to keep things aligned. It covers how the group runs: process, decisions, automation and the website.

The group's deliverables are written in the **working repo** ([W3C-Holon-Community-Group/working-groups](https://github.com/W3C-Holon-Community-Group/working-groups)). Finished assets are promoted to the **official W3C repo** ([w3c-cg/holon](https://github.com/w3c-cg/holon)). This repo holds everything about *how* the group works, so process changes never clutter the deliverables.

> This is a community workspace. Content is licensed as set out in [LICENSE.md](LICENSE.md). The official home of the group is the [W3C Holon Community Group page](https://www.w3.org/groups/cg/holon/). Treat everything posted here as public: Community Group work is meant to be, and everything you contribute is a Contribution under the [W3C Community Contributor License Agreement](https://www.w3.org/community/about/agreements/cla/).

## Participating in three steps

1. **Find.** Open the HCG board and pick your team's view, or the *Help wanted* list if you are new. Anything in **Ready** is fair game.
2. **Claim.** Assign yourself (or comment "I'll take this") and the item moves to **In progress**. Hold no more than two items at a time.
3. **Close.** Open a pull request that links the issue (`Closes #123`). When it merges, the item moves to **Done**.

That's all you need. The PMO does the labelling, triage and tidying. The details are in [CONTRIBUTING.md](CONTRIBUTING.md).

## Asking for something

Open an issue with one of the four forms:

| Form | Use it for |
|---|---|
| **Task** | A piece of work |
| **Decision needed** | A question the group has to settle |
| **Use case** | A new holon use case |
| **Meeting notes** | When the meeting bot missed a meeting |

Not on GitHub? Ask the PMO for a pre-filled issue link, or post to the mailing list ([public-holon@w3.org](mailto:public-holon@w3.org)) and the PMO will turn it into an issue.

## Where the record lives

If it isn't in GitHub or on the W3C mailing list, it hasn't happened yet. Conversations can start anywhere (Substack, LinkedIn, chats), but within a week the outcome should become an issue or a decision file.

| What | Lives in |
|---|---|
| Tasks, requests, questions | Issues and the HCG Project board |
| Decisions | [`decisions/`](decisions/) in this repo |
| Meeting notes | `meetings/` folders in the working repo |
| Specs, Data Book, use cases | Team folders in the working repo, then the W3C repo |
| How the group runs | This repo |

## What's in this repo

| Path | What |
|---|---|
| [CONTRIBUTING.md](CONTRIBUTING.md) | Find, claim, close; the board; Google Docs handoff; promotion |
| [AGENTS.md](AGENTS.md) | Rules for members' AI agents |
| [roadmap.md](roadmap.md) | Quarterly goals |
| [decisions/](decisions/) | One file per group decision |
| [automation/](automation/) | Every automation, with its skill, prompts, runbook and [registry](automation/REGISTRY.md) entry |
| [project/](project/) | Spec for the HCG Project board (fields, views, built-in workflows) |
| [scripts/](scripts/) | One-time setup scripts (labels, Project fields) |
| `.github/` | Issue forms, label definitions, PR template, Actions workflows |
| `site/` | The website (GitHub Pages), coming later |

## Who runs the PMO

| Person | GitHub access | Role |
|---|---|---|
| Christine Connors | Admin | PMO lead; owns the playbook and automations |
| Kurt Cagle | Admin | Second admin; backup owner for automations and org secrets |
| Patrick Audley | Maintainer | Reviews and merges automation and workflow PRs |
| Heather Ray | Admin (backstop) | Emergency access only |

Working-team leads are listed in the HCG contact list and the leadership meeting notes.
