# Prompts

Reusable prompts as plain Markdown, one file per automation: `prompts/<name>.md`.

They are written for people who use whatever AI tool they like. Anyone should be able to paste a prompt into their assistant, add the input it asks for, and get output in the group's template.

## Prompt file shape

```markdown
# <Name> prompt

**Use with:** <what to paste in alongside it: a transcript, an issue list, ...>
**Produces:** <the template it fills, and where the result goes>

---

<the prompt itself>
```

The workflow version of an automation reads the same file, so improving a prompt here improves the automation too.
