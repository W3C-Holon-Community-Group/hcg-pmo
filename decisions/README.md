# Decisions

One file per group decision, named `YYYY-MM-DD-short-title.md` (the date the decision was made), using [`_template.md`](_template.md).

## How a decision gets here

1. Someone opens a **Decision needed** issue: the question, options, deadline and who decides.
2. It is settled in the issue, in a meeting, or on the mailing list.
3. The PMO (or an agent under PMO review) opens a PR adding the decision file, and links it from the issue and from the meeting notes, if there are any.
4. The issue is closed with a link to the merged file.

## Rules

- Decision files are **not edited after merge**, apart from typo fixes and the `superseded_by` field.
- A changed decision is a new file with `supersedes:` pointing to the old one. The old file gets `status: superseded` and `superseded_by:`.
- Decisions that shape a deliverable are linked from the W3C repo when that deliverable is promoted.
