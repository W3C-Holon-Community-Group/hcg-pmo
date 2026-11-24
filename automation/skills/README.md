# Skills

One folder per automation: `skills/<name>/SKILL.md`, plus any helper scripts it needs.

A skill is the instructions an agent follows to do the job by hand, step by step. It is what lets any member's agent (or a person reading it) run the automation when the workflow is down, or when someone new takes it over.

## SKILL.md shape

```markdown
---
name: <name, same as the registry and the workflow file>
description: <one sentence: when to use this skill>
---

# <Name>

## When to use
## Inputs           <!-- what you need before starting: links, files, access -->
## Steps            <!-- numbered, each one checkable -->
## Output           <!-- what exists when you're done, and where -->
## Checks           <!-- how to tell the output is right -->
## Don't            <!-- things that look reasonable but break the record -->
```

Skills follow [AGENTS.md](../../AGENTS.md). They never ask for a personal token.
