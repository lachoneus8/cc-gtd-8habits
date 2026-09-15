# Repository Guidance

This repository combines a GTD workflow with Claude Code commands, optional MCP integrations,
and a progressive 7 Habits / 8th Habit planning layer. The implementation plan and current
phase live in `context/overall_plan.md`.

## Privacy Boundary

Keep information specific to an individual user inside `personal-untracked/`. This includes
identity and values, personal operating context, habit progress, and other user-authored state.
Do not put user-specific details in this file, tracked planning documents, commands, templates,
or other shared implementation files.

Information about how the repository is implemented, how its commands work, or how its plan is
structured belongs in this tracked `CLAUDE.md` or in another tracked documentation file. The
`.gitignore` protects `personal-untracked/` as a directory; preserve that boundary when adding
new private files.

`personal-untracked/` is the *only* place private, runtime-generated content lives — journal
entries, daily logs, weekly reviews, and project files all nest under it
(`personal-untracked/journal/`, `personal-untracked/daily/`, `personal-untracked/weekly/`,
`personal-untracked/projects/active/`, `personal-untracked/projects/archived/`), not at the repo
root. One folder to trust, not several similarly-named ones scattered at the top level. When
adding a new kind of private, generated content, nest it under `personal-untracked/` rather than
creating a new top-level folder for it.

Every file under `personal-untracked/` must open with a standard privacy note, placed as a
blockquote directly beneath the file's own top-level heading:

```markdown
# <File Title>

> Private: this file is private user context for Claude Code. Keep it in `personal-untracked/`;
> do not move its contents into tracked repository guidance.

...
```

This applies whether the file is seeded from a template in `templates/` or created fresh by a
command or skill. `templates/` files that produce `personal-untracked/` output carry the note
already, so it survives being copied; a command or skill that writes a new `personal-untracked/`
file directly (not from a template — e.g. `personal-untracked/todo.md`) must include it too.

## Development Guidance

- Keep the system useful to someone who forks the repository; avoid assumptions about one
  person's identity, schedule, tools, or circumstances.
- Follow the sequencing and scope documented in `context/overall_plan.md`.
- Keep personal values content user-authored. Commands may organize or reflect on it, but should
  not invent or overwrite it without explicit instruction.
- Prefer existing commands, templates, skills, and local conventions before adding new structure.
- Update tracked documentation when a workflow or privacy boundary changes.
