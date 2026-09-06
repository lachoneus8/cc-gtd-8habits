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
- **`context/overall_plan.md`** (this file, tracked) — living statement of the overall
  objective, sequencing philosophy, and current phase. Stays high-level and generic enough to
  make sense to anyone forking the repo.
- **`templates/habits/`** (tracked, not yet created) — planned home for the teaching content of
  each habit: the principle, reflection prompts, and where it hooks into the existing GTD
  mechanics (e.g. Habit 1 → trusting `/capture` and the inbox; Habit 3 → Top 3
  Priorities/time-blocking in `/daily`; Habit 7 → the weekly review and energy management that
  already exist). Built one habit at a time, not drafted in full up front.
- **A personal habit-progress file** (private, not yet created) — tracks which habit is
  current, since progress itself is personal state, not shareable content. Exact shape TBD when
  we get to building the first habit's onboarding.
- **Microsoft To Do** (or whatever daily task tool a given user prefers) — stays the actual
  week-to-week execution surface for some users; this system's `personal-untracked/todo.md`/Todoist/Calendar
  integrations already cover that role for others. How a repo-external tool feeds back and
  forth with this system remains an open, per-user question — not solved here.

## Cadence

Weekly review (`/weekly`) stays the touchpoint, extended over time with a "Habit Calibration"
section alongside the existing "Identity Calibration" once habit content exists to calibrate
against.

## Current phase

**Pre-Habit 1 / Foundation.** Values alignment via `personal-untracked/identity.md`. Habit 1 (Be Proactive)
planning and any new onboarding/command changes start once that foundation is in place —
nothing beyond Habit 1 is being scoped yet.
