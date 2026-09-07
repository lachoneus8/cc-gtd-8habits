# Overall Plan — 7 Habits + GTD

## Objective

Extend [adagradschool/cc-gtd](https://github.com/adagradschool/cc-gtd) with Stephen Covey's
7 Habits (and, later, the 8th Habit) as the values/identity foundation underneath its GTD
execution loop — so the discipline of running GTD has something to anchor to beyond the
mechanics themselves.

This exists for two reasons at once:

1. **Personal.** A prior GTD setup (a different tool, not this repo) lapsed — not because
   capture failed, but because the regular clarify/organize/review discipline did. The premise
   here is that GTD's mechanics need to sit on top of a genuine values foundation to stick this
   time, and that the system should compensate for how people actually operate rather than assume
   willpower or self-monitoring will carry it.
2. **Reusable.** Structured so anyone forking this repo can learn the 7 Habits progressively,
   have GTD's mechanics layered in at the point each habit naturally calls for them, and manage
   the whole thing through a weekly review cadence.

The implementation is tracked in [[task_list]]. The task list stays intentionally concise. Each
habit is built serially through the same five-step loop: gather evidence and best practices,
design the teaching/reflection path, identify the appropriate GTD integration, implement the
LLM-assisted path and private progress state, then validate the habit and its weekly calibration.
The next habit does not begin until the current habit's loop is complete. The "implement" step
for each habit includes updating the shared entry points — `/onboard`, `ONBOARDING.md`, and
`README.md` — so a new user's first-run experience reflects whatever habit layer currently
exists, rather than only the fully-built habits catching up later.

## Sequencing / Approach

- Follow Covey's **inside-out** transformation, in sequence — Private Victory (Habits 1-3)
  before Public Victory (Habits 4-6), with Habit 7 (renewal) ongoing throughout, and Habit 8
  ("Find Your Voice") as a later extension once the core seven are established.
- **Fully build and lock in one habit before moving to the next.** This plan intentionally does
  not lay out habit-by-habit detail beyond the current one — that gets planned/built when we
  get there, for the same reason `/onboard` doesn't dump the entire GTD system on a new user at
  once.
- Foundational, pre-Habit-1 step: values alignment. `personal-untracked/identity.md` (already part of the base
  cc-gtd system, private/gitignored, user-authored) is the natural home for this — it already
  functions as a Habit 2 (mission/roles) artifact, and the weekly review's existing "Identity
  Calibration" already measures present reality against it. That scaffolding is reused as-is
  rather than duplicated with a separate "personal constitution" file.

## Roles of the pieces in play

- **`personal-untracked/identity.md`** (private, user-authored) — the values anchor. Doubles as the Habit 2
  mission/roles artifact.
- **`personal-untracked/repo_context.md`** (private, user-authored) — personal operating context
  and collaboration preferences that must not be copied into the reusable implementation plan.
- **`context/overall_plan.md`** (this file, tracked) — living statement of the overall
  objective, sequencing philosophy, and current phase. Stays high-level and generic enough to
  make sense to anyone forking the repo.
- **`templates/habits/`** (tracked; `README.md` created in `A.1`, per-habit content files not yet
  created) — home for the teaching content of each habit: the principle, reflection prompts,
  practice, and calibration criteria, plus where it hooks into the existing GTD mechanics (e.g.
  Habit 1 → trusting `/capture` and the inbox; Habit 3 → Top 3 Priorities/time-blocking in
  `/daily`; Habit 7 → the weekly review and energy management that already exist).
  `templates/habits/README.md` is the shared model every habit's file follows — written once in
  `A.1`, not redecided per habit. Content itself is still built one habit at a time, not drafted
  in full up front.
- **`/habit`** (new command, not yet created) — introduced when the first habit phase implements
  its LLM-assisted path. On-demand deep-dive session on the user's current-focus habit, alongside
  the lighter touch `/onboard` gives on first exposure and the recurring check-in `/weekly` gives
  via Habit Calibration.
- **A personal habit-progress file** (private, not yet created) — tracks which habit currently
  has the user's focus. Per `A.1`, this field must stay freely changeable and non-terminal:
  moving focus to a new habit is self-declared, with no minimum duration or algorithmic
  threshold, and does not retire the habits already started — their calibration keeps running in
  `/weekly` regardless of current focus. Exact file shape is still TBD (`A.2`).
- **Microsoft To Do** (or whatever daily task tool a given user prefers) — stays the actual
  week-to-week execution surface for some users; this system's `personal-untracked/todo.md`/Todoist/Calendar
  integrations already cover that role for others. How a repo-external tool feeds back and
  forth with this system remains an open, per-user question — not solved here.

## Cadence

Weekly review (`/weekly`) stays the primary touchpoint, extended over time with a "Habit
Calibration" section alongside the existing "Identity Calibration" once habit content exists to
calibrate against. The on-demand `/habit` command supplements this for deliberate deep-dive
sessions; `/onboard` only gives a light first exposure.

## Build vs. Practice — Two Different "Done"s

Decided in `A.1`, this distinction governs how the rest of the plan reads:

- **System build.** Whether a habit's phase (design, GTD integration, LLM-assisted path,
  calibration) is actually implemented is an engineering milestone, checked off via that habit's
  `X.5` validation step in `[[task_list]]`. This governs when the *next* habit's phase begins
  being built — build order stays serial, per the sequencing above.
- **User mastery.** Per Covey's own upward-spiral model, a habit is never "complete" for the
  user, so it is never gated. Once a habit's system support exists it stays live indefinitely.
  See `templates/habits/README.md` for how this reads to the user.

Do not conflate the two: a habit phase finishing `X.5` means the mechanism works, not that the
user has "graduated" the habit.

## Current phase

**Pre-Habit 1 / Foundation.** Values alignment via `personal-untracked/identity.md`. Habit 1 (Be Proactive)
planning and any new onboarding/command changes start once that foundation is in place —
nothing beyond Habit 1 is being scoped yet.
