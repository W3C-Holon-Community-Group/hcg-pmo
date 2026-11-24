# Runbook: <name>

| | |
|---|---|
| **Purpose** | <one sentence> |
| **Trigger** | <schedule / event / manual> |
| **Owner / backup** | <name> / <name> |
| **Workflow** | [`.github/workflows/<name>.yml`](../../.github/workflows/<name>.yml) |
| **Skill** | [`skills/<name>/SKILL.md`](../skills/<name>/SKILL.md) |
| **Secrets used** | <org secret names; never the values> |
| **Last handover test** | <YYYY-MM-DD, by whom> |

## What it does

<!-- Three to six bullets, in the order it does them. -->

## Run it by hand

<!-- How to trigger the workflow manually (Actions → <workflow> → Run workflow), with any inputs. -->

## Do the job without the automation

<!-- The manual path: what a person does, step by step, if the workflow can't run. -->

## How to tell it broke

<!-- Symptoms: a missing issue, a failed run in Actions, an error comment. Where to look first. -->

## Fix it

| Symptom | Likely cause | Fix |
|---|---|---|
| | | |

## Switch it off

<!-- Actions → <workflow> → ⋯ → Disable workflow. Say what stops happening, and who to tell. -->

## Hand it over

<!-- What a new owner needs: access, secrets to rotate, people to tell. Update the registry. -->
