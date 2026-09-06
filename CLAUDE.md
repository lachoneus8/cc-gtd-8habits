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

## Development Guidance

- Keep the system useful to someone who forks the repository; avoid assumptions about one
  person's identity, schedule, tools, or circumstances.
- Follow the sequencing and scope documented in `context/overall_plan.md`.
- Keep personal values content user-authored. Commands may organize or reflect on it, but should
  not invent or overwrite it without explicit instruction.
- Prefer existing commands, templates, skills, and local conventions before adding new structure.
- Update tracked documentation when a workflow or privacy boundary changes.
