# Weekly Review Template

Review the week's accomplishments and plan for the next week.

Ensure context is synced with Todoist and Google Calendar.
Invoke the `/todoist` and `/calendar` skills before proceeding with the review.

Add a new log file for the week in `personal-untracked/weekly/` folder with name like
`2025-W28.md`. Open a new file with the standard privacy header:

```markdown
# Weekly Review - 2025-W28

> Private: this file is private user context for Claude Code. Keep it in `personal-untracked/`;
> do not move its contents into tracked repository guidance.
```

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
- **Habit Calibration**: measure present self against each started habit's Calibration Criteria (see below).

## Review Checklist

- [ ] Process inbox to zero
- [ ] Review all projects for next actions
- [ ] Check waiting-for items for follow-ups
- [ ] Review someday-maybe for activation
- [ ] Update calendar for upcoming week
- [ ] Clean up completed items
- [ ] Check Scheduled Sessions (below)
- [ ] Run the Identity Calibration (below)
- [ ] Run the Habit Calibration (below)

## Scheduled Sessions

Scan `personal-untracked/calendar.md`'s `## Time-Specific Items` for `(Session)`-tagged lines —
big-effort commitments deferred from `/onboard` or elsewhere (e.g. the GTD full capture sweep).

1. For any `(Session)` line still unchecked with a date on or before today, ask whether it
   happened. If yes, check it off. If not, ask whether to move it to a new date (edit the date in
   place) or drop it — don't just silently carry it forward unasked.
2. For any `(Session)` line with a future date, no action needed — just note it exists if it's
   coming up this week.
3. If `personal-untracked/calendar.md` doesn't exist yet, say so and skip this section.

## Identity Calibration

Measure present self against the durable identity in `personal-untracked/identity.md`.

1. Read `personal-untracked/identity.md` and the week's `personal-untracked/journal/` entries (especially any
   `### Brain Dump on Open Loops` from `/restart`).
2. For each identity statement, assess present reality from journal evidence and the week's
   actual behavior. Quote my own words where possible — don't paraphrase me into something
   tidier than I said.
3. Produce a status table: identity | present reality (my words) | status
   (🟢 Aligned · 🟡 Drifting · 🔴 Off) | gap | one keystone action.
4. **Diff against last week's calibration** (the previous `personal-untracked/weekly/` file's calibration
   section): what moved 🔴→🟡→🟢 or slipped back? Name the trend, not just the snapshot.
5. End with a short verdict and the keystone(s) to move _this_ week — usually the smallest
   number of root causes that unlock the most downstream loops.

Write the calibration into this week's `personal-untracked/weekly/` file (don't create a separate review
file). Be honest, specific, direct — match my own vocabulary, not therapy-speak. If
`personal-untracked/identity.md` doesn't exist yet, say so and skip this section.

## Habit Calibration

Follows the Weekly Calibration Contract in `habits/README.md`. If
`personal-untracked/habits.md` has no Started Habits yet, say so and skip this section.

1. Read `personal-untracked/habits.md` for Current Focus and every Started habit, and this
   week's `personal-untracked/journal/`/`personal-untracked/daily/` entries.
2. For the **Current Focus** habit only, go full depth using its Calibration Criteria from
   `habits/habit<N>.md`:
   - Status table: criterion | present reality (my words) | status
     (🟢 Aligned · 🟡 Drifting · 🔴 Off) | gap | one keystone action.
   - Diff against last week's Habit Calibration for this same habit — name the trend, not just
     the snapshot.
   - End with a verdict and the keystone action(s) to move this week.
3. For **every other Started habit**, one line each: habit name, status (🟢/🟡/🔴), one-word
   trend vs. last week (↑/↓/→). No table, no keystone action.
4. If any light-touch habit has been 🔴 or 🟡 for multiple weeks running, offer to schedule a
   deep-dive `/habit` session for it as a `(Session)` line in `personal-untracked/calendar.md`
   (see "Scheduled sessions" in `[[overall_plan]]`) — offer, don't add it unasked.

Write the calibration into this week's `personal-untracked/weekly/` file, next to Identity Calibration. Same voice:
honest, specific, direct, no therapy-speak, no inflating status to look better than it is.

## This Week's Accomplishments

<!-- Major completions and progress -->

## Next Week's Focus

<!-- Key priorities and commitments -->

## System Health

- Inbox items processed:
- Projects with next actions:
- Overdue waiting-for items:
- System trust level (1-10):
