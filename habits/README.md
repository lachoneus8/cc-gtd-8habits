# Habit Content

Home for both the research behind each of the 7 Habits (and later the 8th Habit) and the actual
teaching/reflection/practice content built from it. One file per habit — `habitN.md` (e.g.
`habit1.md`, `habit8.md` for the 8th Habit) — covering both, so a habit's design decisions stay
next to the evidence that led to them instead of split across files.

## Shape of a habitN.md File

- **Research** — best-practices research gathered for that habit's `.1` task (see
  `[[overall_plan]]` for the standing web-research requirement). Covers the core concept
  grounded in Covey's text, practitioner exercises, cross-disciplinary grounding, common
  pitfalls/misapplications, and sources. Feeds the Habit Content below; not itself shown to the
  user.
- **Habit Content** — the shipped content, read directly by `/onboard`, `/habit`, and `/weekly`'s
  Habit Calibration, never copied into `personal-untracked/`:
  - **Principle** — the core idea in plain language, not a book summary or a long quote.
  - **Reflection Prompts** — a small set of concrete questions to sit with, not a form to fill
    out.
  - **Practice** — one or two concrete things to actually do.
  - **Calibration Criteria** — what `/weekly` looks for as evidence of the habit, drawn from
    your own journal and daily entries, assessed 🟢 Aligned / 🟡 Drifting / 🔴 Off, and compared
    against last week so you can see the trend, not just a snapshot.

## How Habit Coaching Reaches You

- **`/onboard`** introduces the values foundation and, later, your current habit at a light
  level — it doesn't try to teach everything at once.
- **`/weekly`** is where habit coaching mainly lives day to day: a "Habit Calibration" section,
  alongside the existing Identity Calibration, checks in on every habit you've started, not just
  the one that currently has your focus.
- **`/daily`** adds one short habit question every few days (not every day), so the habit
  stays in view between weekly reviews. See "Daily Habit Prompt Contract" below.
- **`/habit`** is there when you want a deliberate session: revisit a habit's core idea, work
  through its reflection prompts, log practice. Practice notes land under that habit's own
  section in your `personal-untracked/habits.md`, so its history stays together with the habit.
- Individual habits also show up inside the everyday GTD commands where they naturally apply —
  for example, Habit 1 shapes how `/capture` talks about trusting the inbox, Habit 2 shapes how new projects get a Desired Outcome and how `/weekly` reads your Roles and Mission, Habit 3 shapes
  time-blocking in `/daily`, and so on.

## Weekly Calibration Contract

The process `/weekly`'s "Habit Calibration" section follows once it's built — the same shape
Identity Calibration already uses in `.claude/commands/weekly.md`, generalized so every habit
reuses it rather than each one reinventing its own review logic.

- **Scope.** Every habit in Started Habits gets checked each week, not just Current Focus — but
  not all at the same depth (see below).
- **Full depth — Current Focus habit only:**
  1. Evidence comes from journal/daily entries in the user's own words, quoted, not paraphrased
     into something tidier.
  2. Status table: this habit's Calibration Criteria | present reality (their words) | status
     (🟢 Aligned / 🟡 Drifting / 🔴 Off) | gap | one keystone action for the week.
  3. Diff against last week's calibration for this same habit — name the trend, not just the
     snapshot.
  4. End with a verdict and the keystone action(s) to move this week.
- **Light touch — every other started habit:** one line — habit name, status
  (🟢/🟡/🔴), one-word trend vs. last week (↑/↓/→). No table, no keystone action, unless status
  has been 🔴/🟡 for multiple weeks running — that's the trigger for `/weekly` to suggest a
  scheduled deep-dive session (see "Scheduled sessions" in `[[overall_plan]]`), not something to
  handle inline in the calibration line itself.
- **Where it's written.** The same `personal-untracked/weekly/YYYY-Www.md` file, in a "## Habit
  Calibration" section alongside "## Identity Calibration" — never a separate file, matching how
  habit calibration history already stays in `personal-untracked/weekly/` rather than duplicated
  in `habits.md`.
- **Guard.** If Started Habits is empty, say so and skip the section, same as Identity
  Calibration does when `identity.md` doesn't exist yet.

## Daily Habit Prompt Contract

`/weekly` is the main touchpoint, but a week is a long gap for a habit meant to shape daily
choices. `/daily` adds one short, occasional question so the habit stays in view between reviews.
It is deliberately not every day.

- **Scope.** The Current Focus habit only, and only when `personal-untracked/habits.md` has at
  least one Started Habit. Otherwise `/daily` says nothing about it.
- **Cadence.** Kept in the user's `personal-untracked/habits.md` under `## Daily Prompt`:
  `Cadence` (the minimum days between prompts, default 3), `Last prompted` (a date), and
  `Last prompt` (the question text). `/daily` prompts only once the cadence has elapsed and stays
  silent on the days in between. The user changes the cadence by editing the file or telling the
  assistant.
- **The question.** Exactly one, in plain language, drawn from the habit's Reflection Prompts or
  Calibration Criteria in `habits/habit<N>.md`. Tie it to something real in the day's plan or
  yesterday's log when possible (a stalled loop, a waiting thread) so it doesn't read as generic.
  Never repeat the last prompt. It's a question to sit with, not a form to fill out.
- **Where it lands.** A `### Habit Check-in` section in the daily log. The user can answer in the
  log's `## Reflection` or in chat. Skipping it is fine: no nagging, no carry-over.
- **What happens to answers.** The next `/daily` notes an answer found in a recent Reflection and
  offers (never silently writes) to add it to the habit's Practice Log. `/weekly`'s Habit
  Calibration quotes these answers as evidence.
- **Independent of `/shutdown`.** The check-in works with only `/daily` and `/weekly`, since not
  everyone ends their day with a shutdown ritual.
- **Voice.** Same as the calibration: direct, specific, no therapy-speak.

## Moving Between Habits

There's no finish line here — Covey's own model treats these as habits you keep deepening, not
boxes you check once and set aside. Move your primary focus to a new habit whenever you feel
ready. The habits you've already started don't drop out of `/weekly`'s calibration, and returning
to an earlier one at a deeper level later is expected, not backsliding.

## Voice

Calibration and coaching match the tone already used in Identity Calibration: direct,
evidence-based from your own words, no therapy-speak, no inflating status to look better than it
is.
