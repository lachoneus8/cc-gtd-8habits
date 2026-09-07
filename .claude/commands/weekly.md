# Weekly Review Template

Review the week's accomplishments and plan for the next week.

Ensure context is synced with Todoist and Google Calendar.
Invoke the `/todoist` and `/calendar` skills before proceeding with the review.

Add a new log file for the week in `weekly/` folder with name like `2025-W28.md`

## Usage

```
/weekly
```

## Features

- **Interactive Review**: AI-powered review of the week's accomplishments
  - Add a weekly review section going over last week's accomplishments, areas of improvements, meta trends
  - Add a section that goes over each active project's `info.md` (progress) and `tasks.md` (next actions) to ensure sync. Add `EDIT` blocks to get feedback from me.
  - Once you've the feedback then process those to update the project's `info.md` and `tasks.md` files.
  - Then plan the next week.
- **Identity Calibration**: measure present self against `personal-untracked/identity.md` (see below).

## Review Checklist

- [ ] Process inbox to zero
- [ ] Review all projects for next actions
- [ ] Check waiting-for items for follow-ups
- [ ] Review someday-maybe for activation
- [ ] Update calendar for upcoming week
- [ ] Clean up completed items
- [ ] Run the Identity Calibration (below)

## Identity Calibration

Measure present self against the durable identity in `personal-untracked/identity.md`.

1. Read `personal-untracked/identity.md` and the week's `journal/` entries (especially any
   `### Brain Dump on Open Loops` from `/restart`).
2. For each identity statement, assess present reality from journal evidence and the week's
   actual behavior. Quote my own words where possible — don't paraphrase me into something
   tidier than I said.
3. Produce a status table: identity | present reality (my words) | status
   (🟢 Aligned · 🟡 Drifting · 🔴 Off) | gap | one keystone action.
4. **Diff against last week's calibration** (the previous `weekly/` file's calibration
   section): what moved 🔴→🟡→🟢 or slipped back? Name the trend, not just the snapshot.
5. End with a short verdict and the keystone(s) to move _this_ week — usually the smallest
   number of root causes that unlock the most downstream loops.

Write the calibration into this week's `weekly/` file (don't create a separate review
file). Be honest, specific, direct — match my own vocabulary, not therapy-speak. If
`personal-untracked/identity.md` doesn't exist yet, say so and skip this section.

## This Week's Accomplishments

<!-- Major completions and progress -->

## Next Week's Focus

<!-- Key priorities and commitments -->

## System Health

- Inbox items processed:
- Projects with next actions:
- Overdue waiting-for items:
- System trust level (1-10):
