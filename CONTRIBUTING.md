# Contributing to HCG

HCG is run by volunteers. These rules are kept short on purpose: contributors only need to **find, claim and close**. Everything else (labels, triage, sync, housekeeping) is the PMO's job.

Before you post anything, remember that Community Group repositories, mailing lists and minutes are meant to be **public**, and everything you contribute falls under the [W3C Community Contributor License Agreement](https://www.w3.org/community/about/agreements/cla/). Keep employer-confidential and proprietary material out.

## Principles

- **One home for the work.** Work happens in the working repo. Done assets are promoted to the W3C repo. Google Drive is being retired.
- **Pull, don't push.** You pick up work when you have time. Nobody is assigned work they did not opt into.
- **Visible over complete.** A rough issue that exists beats a perfect one that doesn't.
- **Default to asynchronous.** Meetings decide and unblock. Everything else happens in issues and pull requests.

## The board

One HCG Project board covers this repo and the working repo, with a view per working team.

| Status | Means | How an item gets there |
|---|---|---|
| **Inbox** | New and untriaged | Anyone opens an issue |
| **Ready** | Clear enough to pick up | It has a team label and a one-line "done when" |
| **In progress** | Someone is actively on it | Someone volunteered and is assigned |
| **In review** | Needs eyes or a group decision | A PR or comment asks for review |
| **Done** | Closed | Merged, decided, or closed with a reason |
| **Parked** | Valid, but nobody has time for it | The PMO or a team lead parks it |

Parking is not failure. It keeps **Ready** honest.

### Light limits

- **Work in progress:** hold no more than **2** items in progress at once. This is guidance, not enforcement.
- **Staleness:** after **30 days** with no activity, an item gets a friendly nudge. After **45 days** it goes back to Ready and is unassigned, with no blame. *(Provisional: the 30/45-day rule is still being confirmed with the group.)*
- **No estimates.** If size matters, add `size:small`, `size:medium` or `size:large`.

## Find, claim, close

### Find

- Your team's board view shows everything for your team.
- New here? The *Help wanted* view lists items labelled `good-first-issue` and `help-wanted`.

### Claim

Assign yourself, or comment "I'll take this" and the PMO will assign you. If you can't continue, unassign yourself or say so in a comment. Nobody minds.

### Close

Open a pull request and put `Closes #<issue>` in the description. For work in another repo, use the full form: `Closes W3C-Holon-Community-Group/hcg-pmo#12`. Merging the PR closes the issue and moves it to **Done**. For non-code work (a decision, a question answered), close the issue with a one-line reason.

## Labels

The PMO applies labels. You don't have to, but you may.

| Group | Labels |
|---|---|
| Team | `team:core-spec`, `team:data-book`, `team:harmonization`, `team:identity`, `team:industry`, `team:network-arch`, `team:serialization`, `team:shared`, `team:pmo` |
| Type | `type:task`, `type:decision`, `type:use-case`, `type:notes` |
| Lifecycle | `ready-to-promote`, `promoted` |
| Help | `good-first-issue`, `help-wanted`, `blocked` |
| Size (optional) | `size:small`, `size:medium`, `size:large` |

The full definitions, with colours and descriptions, are in [`.github/labels.json`](.github/labels.json).

## Decisions

Any question the group needs to settle starts as a **Decision needed** issue, with the options, a deadline and who decides. Once it is decided, the outcome is recorded as a file in [`decisions/`](decisions/) using the [template](decisions/_template.md), and the issue is closed with a link to that file. Decision files are not edited after merge. A changed decision is a new file that says which one it supersedes.

## Meeting notes

Every meeting should leave three things in the working repo: **notes**, **decisions** and **action items as issues**.

- The meeting bot (Read.ai) is the default way to capture them. The bot should be on the calendar series, not added each time.
- If the bot missed a meeting, any attendee fills in the **Meeting notes** issue form. Bullets are enough.
- Notes land through a pull request as `YYYY-MM-DD.md` in the matching `meetings/` folder of the working repo: the team's own folder (for example `Identity/meetings/`), `pmo/meetings/` for PMO meetings, or `plenaries/meetings/` for full-group meetings.
- The PMO (or an agent under PMO review) turns each action into an issue with the team label, each decision into a decision file, and links them all from the notes PR.

Attendees should only ever need to supply raw notes.

## Google Docs: the handoff rule

Co-drafting in a Google Doc is fine while an idea is rough, as long as the Doc is **linked from an issue**. When it is ready for review:

1. Move its content into a pull request as Markdown.
2. Put this banner at the top of the Doc: *Moved to GitHub, see [link]. Do not edit here.*
3. Move any open Doc comments into the issue. Drive comments are not synced.

New documents should start in GitHub. Drive is read-only once migration finishes.

## Promotion to the W3C repo

When a team lead considers an asset done, they label its issue `ready-to-promote`. A pull request is then opened on [w3c-cg/holon](https://github.com/w3c-cg/holon). Someone with rights there reviews and merges, and the source issue is labelled `promoted`.

*Still open:* the group has not yet agreed what "done" means for promotion, or who merges in the W3C repo. Until it has, ask the PMO before labelling something `ready-to-promote`.

## AI agents

Agents are welcome contributors under the same rules as people, plus clear labelling. Read [AGENTS.md](AGENTS.md) before you let an agent open issues or PRs.

## Channels

| Channel | Use it for | Part of the record? |
|---|---|---|
| GitHub issues, PRs, decision files | Work, review, decisions | Yes, the primary record |
| GitHub Discussions *(proposed)* | Cross-team questions, announcements, ideas | Yes |
| W3C mailing list ([public-holon@w3.org](mailto:public-holon@w3.org)) | Formal notices, weekly digest, calls for review | Yes, the official public record |
| Substack, LinkedIn | Outreach that links back to GitHub or the W3C repo | No |
| Private chats, DMs | Working ideas out | No: within a week, the outcome becomes an issue or a decision file |

## Changing these rules

Open a **Decision needed** issue in this repo. Each new rule should answer a problem the group actually had.
