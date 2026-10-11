# Daily Plan

Create and update today's daily plan with prioritized tasks and time blocks.

Ensure context is synced with Todoist and Google Calendar.
Invoke the `/todoist` and `/calendar` skills before proceeding with the daily plan.

**Always start by copying the daily skeleton from `personal-untracked/calendar.md`** into today's `### Time
Blocks` as the fixed scaffold. Then layer the day's prioritized tasks onto and between
those blocks — don't replace the skeleton, build on it. If today is a weekend, treat the
skeleton as optional and keep the day open for breadth.

**Check `personal-untracked/waiting-for.md`** for items with a follow-up date on or before today.
Surface each as a Top 3 candidate or a Heads-up note ("follow up with X — no response since
<date>") rather than silently carrying it. Don't touch waiting-for.md itself here; checking off or
resolving an item happens when I report the outcome, not automatically.

**Then create/refresh `personal-untracked/todo.md`** — the flat, live working list for today (see
below). This is the file I keep updating through the day; `/shutdown` reconciles it in the
evening.

## `personal-untracked/todo.md` — today's working list

Every `/daily` run (re)generates `personal-untracked/todo.md`: a single, dead-simple checklist
of just *today's* actionable tasks, flattened from the Top 3 + time-block tasks. No prose,
no projects, no time blocks — just checkboxes I can tick and add to all day.

- Overwrite `personal-untracked/todo.md` fresh each morning. First, carry over any unchecked items from
  yesterday's `personal-untracked/todo.md` (they didn't get done) before adding today's.
- Tag each line with its source project in parens so `/shutdown` can route completions back,
  e.g. `- [ ] Send renewal paperwork (Admin)`.
- Keep a `## Captured` section at the bottom empty for me to jot new loops during the day.

Template:

```markdown
# Todo — YYYY-MM-DD

> Private: this file is private user context for Claude Code. Keep it in `personal-untracked/`;
> do not move its contents into tracked repository guidance.

## Top 3

- [ ] … (Project)

## Today

- [ ] … (Project)

## Captured

<!-- jot new tasks/loops here during the day; /shutdown processes them -->
```

## Habit check-in (not every day)

Keep the habit practice in view between weekly reviews. Follows the Daily Habit Prompt Contract in
`habits/README.md`; the short version:

- **Guard.** Only if `personal-untracked/habits.md` has at least one Started Habit. Otherwise skip
  silently.
- **Cadence.** Read `## Daily Prompt` in `personal-untracked/habits.md` (`Cadence` = minimum days
  between prompts, default 3; `Last prompted`; `Last prompt`). Add the check-in only when at least
  that many days have passed since `Last prompted`. On other days say nothing about it.
- **One question.** Take it from the Current Focus habit's Reflection Prompts or Calibration
  Criteria in `habits/habit<N>.md`, and tie it to something real in today's plan or yesterday's
  log when you can. Plain language, one question, not a form. Don't repeat `Last prompt`.
- **Where it goes.** A `### Habit Check-in` section in the daily log, after Heads-up. I can answer
  in the log's `## Reflection` or in chat; skipping it is fine, and don't carry it over.
- **Close the loop.** Then update `Last prompted` and `Last prompt` in
  `personal-untracked/habits.md`. If the previous prompt got an answer in a recent daily log's
  `## Reflection`, note it briefly and offer (don't silently write) to add it to that habit's
  Practice Log. `/weekly`'s Habit Calibration uses these answers as evidence.
- This does not depend on `/shutdown`.

## Usage

```
/daily
```

## Features

- **Smart Task Selection**: Pulls high-priority items from project `tasks.md` files
- **Energy Mapping**: Schedules tasks based on optimal energy levels
- **Time Blocking**: Creates structured focus sessions
- **Project Integration**: Reviews all active projects' `info.md` for status and `tasks.md` for next actions

## Daily Plan Structure

```markdown
# Daily Log - 2025-06-26

> Private: this file is private user context for Claude Code. Keep it in `personal-untracked/`;
> do not move its contents into tracked repository guidance.

## 📋 Daily Plan

**Last Updated:** 09:15

### Top 3 Priorities

1. [ ] Complete user authentication debugging
2. [ ] Client presentation preparation
3. [ ] Team check-in meetings

### Time Blocks

- **09:00-10:30** High Energy Block
  - [ ] @work-code: Debug authentication system
  - [ ] @work-code: Write unit tests for auth module
- **10:45-12:00** Deep Work Block
  - [ ] @work-computer: Prepare client presentation slides
- **14:00-15:30** Communication Block
  - [ ] @work-calls: Team check-in
  - [ ] @work-calls: Client status update call

### Energy Mapping

- **High Energy (9-11am)**: Complex coding tasks
- **Medium Energy (11am-3pm)**: Presentations, planning
- **Low Energy (3-5pm)**: Emails, administrative work

### Habit Check-in (only on prompt days)

Where have you caught yourself saying "I have to" this week, and what would the proactive version
of that sentence be?
```

## AI Optimization

- Analyzes task complexity and energy requirements
- Suggests optimal scheduling based on typical energy patterns
- Identifies dependencies and suggests task ordering
- Provides realistic time estimates based on similar past tasks
- Flags potential scheduling conflicts

## Update Behavior

- Creates new daily log if none exists for today
- Updates existing plan while preserving work log entries
- Suggests plan adjustments based on completed/remaining work
- Maintains plan history with timestamps
