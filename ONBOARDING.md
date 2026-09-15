# Onboarding

Run the guided command from Claude Code:

```text
/onboard
```

That command is the source of truth for first-run setup. It creates or checks the private
workspace, walks through identity anchors, project setup, calendar skeleton, first brain
dump, first processed actions, and the first daily plan.

## What You Are Building

This is not a normal todo list. It is a GTD operating loop:

```text
/restart -> /capture -> /daily -> personal-untracked/todo.md -> /shutdown -> /weekly
```

- `personal-untracked/journal/` is raw thinking.
- `personal-untracked/inbox.md` is unprocessed capture.
- `personal-untracked/projects/active/*/info.md` holds outcomes and status.
- `personal-untracked/projects/active/*/tasks.md` holds next actions by context.
- `personal-untracked/calendar.md` mirrors fixed commitments and recurring blocks.
- `personal-untracked/todo.md` is only today's working list.
- `personal-untracked/daily/` records plan, work log, and reflection.
- `personal-untracked/weekly/` keeps the system honest.

Underneath this loop, `personal-untracked/identity.md` is the values/identity anchor the weekly
review calibrates against. This fork layers Stephen Covey's 7 Habits (and later the 8th Habit) on
top of that foundation progressively — one habit built and locked in at a time, not all at once.
See [context/overall_plan.md](context/overall_plan.md) for the current phase.

Once a habit has content built (Habit 1: Be Proactive is first), run `/habit` any time for a
deliberate session on it — its own core idea, reflection prompts, and practice, logged to
`personal-untracked/habits.md`. `/weekly` also picks up a Habit Calibration section once that
habit's practice log has something to calibrate against.

## First-Run Short Version

```bash
just setup
```

Then in Claude Code:

```text
/onboard
```

MCP integrations are optional. Start with local markdown first; connect Todoist, Google
Calendar, or Slack once the basic loop works.

## Privacy

Personal files are intentionally ignored by git. After setup, `git status --ignored` should
show the `personal-untracked/` folder, private runtime folders, and local MCP config as ignored.
