# AGENTS.md

Rules for AI agents working in HCG repositories: coding agents, chat assistants with GitHub access, and scripted automations. Many agents read this file automatically. If yours doesn't, point it here before it touches an HCG repo.

Agents are welcome contributors. They follow the same rules as people in [CONTRIBUTING.md](CONTRIBUTING.md), plus the rules below.

## Context

- HCG is a W3C Community Group. Treat its repositories, issues, mailing lists and minutes as **public**, and every contribution falls under the [W3C Community Contributor License Agreement](https://www.w3.org/community/about/agreements/cla/).
- Repositories:
  - `W3C-Holon-Community-Group/working-groups`: the working repo, where deliverables and meeting notes are written.
  - `W3C-Holon-Community-Group/hcg-pmo`: this repo; process, decisions and automation.
  - `w3c-cg/holon`: the official W3C repo. Agents do not open PRs here directly; promotion goes through the `ready-to-promote` flow.

## Rules

### 1. Work through pull requests and issues only

- Never push to `main`. Work on a branch and open a pull request.
- Never merge a pull request, close someone else's issue, or change labels on an item in **Done**.
- Do not change `.github/workflows/`, repository settings or secrets unless the member responsible asked for exactly that change in the issue you are working on.

### 2. Say an agent did it

Every commit, pull request, issue and comment written by an agent says which agent and which member is responsible:

- **PR and issue descriptions, comments:** end with `Drafted by <agent> for @<member>`.
- **Commits:** add a trailer, for example:

  ```
  Drafted-by: <agent name and version>
  On-behalf-of: @<member>
  ```

- On the Project board, set the **Source** field to `Agent`.

### 3. A human owns every agent contribution

The member whose agent opened a PR or issue is its assignee and answers review comments. An agent contribution with no responsible member may be closed without review.

### 4. Use the templates

Notes, decisions and use cases follow the repo templates so automation can parse them. Keep the section headings and their order, even when a section is empty.

| Artifact | Template | Lands in |
|---|---|---|
| Meeting notes | HCG meeting-notes templates (working-team, leadership, full group) | `YYYY-MM-DD.md` in the matching meetings folder of the working repo (see CONTRIBUTING.md) |
| Decision | [`decisions/_template.md`](decisions/_template.md) | `decisions/YYYY-MM-DD-short-title.md` in this repo |
| Use case | Use-case template (v2) | `HCG Administration/Use Cases/UC-XXX-short-title.md` in the working repo |
| Issue | One of the four issue forms | Inbox on the board |

File and folder names: dates are `YYYY-MM-DD`; slugs are lowercase kebab-case.

### 5. Respect the record

- Summarize; don't rewrite. Never change the substance of a decision file, or anyone else's meeting notes, after they are merged. Corrections go in a new PR that says what changed and why.
- When drafting notes from a transcript, attribute positions to people only if the transcript makes them clear. When unsure, leave them unattributed.
- Never invent attendees, decisions, owners or dates. Leave a field blank and flag it in the PR description.

### 6. Mind confidentiality

- Nothing from a member's employer goes into prompts, issues or the repo unless it is already public.
- Don't paste private chats, DMs or email threads into the repo. Summarize the outcome and link to the public record instead.
- Use synthetic or anonymized data in examples.

### 7. Stay within scope

- One issue, one PR. Don't bundle unrelated changes.
- Don't do mass edits (relabelling, closing, reformatting across many files) without a **Task** issue that a PMO member has approved.
- Prefer small, reviewable PRs.

## Good jobs for agents

- Inbox triage suggestions: team label, type, likely duplicates. Leave them as a comment; the PMO applies labels.
- Turning raw notes or a transcript into the notes template.
- Drafting decision records from a merged notes PR.
- Drafting the weekly digest.
- Checking links on the website and in the working repo.

## Automations

Group automations live in [`automation/`](automation/). An agent running one follows that automation's `SKILL.md` and runbook, and uses only group-owned credentials (org secrets, the HCG bot account or GitHub App), never a member's personal token.
