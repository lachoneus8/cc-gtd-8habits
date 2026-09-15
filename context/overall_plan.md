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

**The "gather best practices" step (each phase's `.1` task) always includes web research, not
just what's already understood about the book.** Search for how practitioners, coaches, and
adjacent fields (psychology, philosophy, workplace application) have applied that habit since
the book's publication — concrete exercises, common pitfalls, and where other traditions
independently arrive at the same principle. Everything found still has to stay rooted in Covey's
actual text; research that contradicts or dilutes the core idea gets noted as a caution, not
adopted as a substitute. Write the findings to `habits/habit<N>.md` (tracked — this is
research, not personal content) before B.2/C.2/D.2/… starts designing that habit's actual
teaching/reflection/practice content. The best-practices file is raw material for that design
step, not the habit's shipped content itself, and should say so.

Habit 1's phase (Phase B) has a sixth step the rest don't: validating the whole foundation path
end to end (B.5), before validating Habit 1 itself (B.6). This is deliberate, not a template for
later habits — `/onboard` is meant to launch a new user straight into Habit 1, so the foundation
only makes sense to validate end-to-end once Habit 1 actually exists to onboard into. Habits 2
onward go back to the plain five-step loop.

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
- **Onboarding is staged, not one-shot.** Both source authors say the same thing in their own
  domain: Covey expects one read-through of the whole book for structure, then real work
  happens one habit at a time; Allen expects a dedicated, sized-for-real-life session to do the
  initial full capture rather than assuming it happens inline. A single `/onboard` run should
  not try to force either of those into one sitting. Three stages: **(1) Foundation** — the light
  scaffolding and first trustworthy loop `/onboard` already builds in one sitting; **(2) Full
  Capture Sweep** — GTD's initial full capture, deferred to a scheduled session (see "Scheduled
  sessions" below) sized to when the user actually has the time, not forced inline; **(3) Habit
  Deep Dives** — ongoing, on-demand via `/habit` as each habit becomes Current Focus, with no
  fixed schedule of its own.
- **Assumed prior reading.** The system assumes the user has read *The 7 Habits of Highly
  Effective People* (30th Anniversary Edition, which briefly covers the 8th Habit) and David
  Allen's *Getting Things Done* (2015 edition). Content and
  coaching should teach application against this system, not re-explain either methodology's
  fundamentals from scratch.

## Roles of the pieces in play

- **`personal-untracked/identity.md`** (private, user-authored) — the values anchor. Doubles as the Habit 2
  mission/roles artifact.
- **`personal-untracked/repo_context.md`** (private, user-authored) — personal operating context
  and collaboration preferences that must not be copied into the reusable implementation plan.
- **`context/overall_plan.md`** (this file, tracked) — living statement of the overall
  objective, sequencing philosophy, and current phase. Stays high-level and generic enough to
  make sense to anyone forking the repo.
- **`habits/`** (tracked; `README.md` and `habit1.md` created, `habit2.md` onward not yet) — one
  file per habit (`habitN.md`) holding both the best-practices research behind it and the
  teaching content built from that research: the principle, reflection prompts, practice, and
  calibration criteria, plus where it hooks into the existing GTD mechanics (see the GTD
  Integration Map below). Deliberately one file, not a research file plus a separate content
  file — keeps a habit's design decisions next to the evidence that led to them. `habits/README.md`
  is the shared model every habit's file follows — written once, not redecided per habit.
  Content itself is still built one habit at a time, not drafted in full up front. Read directly
  by `/onboard`, `/habit`, and `/weekly` — never copied into `personal-untracked/`, and distinct
  from `personal-untracked/habits.md` below despite the similar name: this directory is shared
  content, that file is private per-user state.
- **`/habit`** (new command, not yet created) — introduced when the first habit phase implements
  its LLM-assisted path. On-demand deep-dive session on the user's current-focus habit, alongside
  the lighter touch `/onboard` gives on first exposure and the recurring check-in `/weekly` gives
  via Habit Calibration.
- **`personal-untracked/habits.md`** (private, template at `templates/habits.md`) — tracks
  Current Focus (which habit has the user's attention now; self-declared,
  freely changeable, LLM writes it only on explicit instruction) and Started Habits (one section
  per habit begun, each with its own dated Practice Log accumulated from `/habit` sessions). A
  habit can only be added to Started Habits once its content exists under `habits/`.
  Calibration history is not duplicated here — it stays in `personal-untracked/weekly/`, same as Identity
  Calibration. Unlike `identity.md`, this file is system-managed state the LLM may write, not
  user-authored content it must never invent.
- **Scheduled sessions** — the deferred-work counterpart to the staged-onboarding principle
  above. Big-effort items that don't fit inside `/onboard` or a single `/habit` run (GTD's
  initial full capture sweep, later a deeper per-habit practice pass) need somewhere to live as
  a concrete, sized commitment rather than an open-ended intention that quietly never happens.
  No new file: a scheduled session is a `(Session)`-tagged line in
  `personal-untracked/calendar.md`'s existing `## Time-Specific Items`
  (`- [ ] YYYY-MM-DD — Description (Session)`), checked off once done. `/onboard` offers one for
  the GTD full capture sweep at close of onboarding (optional, never forced); `/weekly` gets a
  generic checklist step that surfaces any `(Session)` line that's overdue or unchecked and asks
  whether it happened or should move. This mechanism is habit-agnostic and already active. The
  second use case — `/weekly`'s Habit Calibration suggesting a scheduled deep-dive session after
  sustained drift on a habit — reuses the same `(Session)` convention but is not wired up yet:
  Habit Calibration itself doesn't exist until [[task_list]] A.4/Phase B build it.
- **Microsoft To Do** (or whatever daily task tool a given user prefers) — stays the actual
  week-to-week execution surface for some users; this system's `personal-untracked/todo.md`/Todoist/Calendar
  integrations already cover that role for others. How a repo-external tool feeds back and
  forth with this system remains an open, per-user question — not solved here.

## GTD Integration Map

The GTD mechanics this repo forked from ([adagradschool/cc-gtd](https://github.com/adagradschool/cc-gtd))
are already mature — nothing below requires new GTD infrastructure. This is a pointer, not a
build: it names which *existing* command or file each habit's own phase (the "identify the
appropriate GTD integration" step, e.g. B.3/C.3/D.3…) hooks into when that habit is actually
built. The habit's own phase still does the real integration work in full; this just says where.

| Habit | Existing GTD hook |
|---|---|
| 1. Be Proactive | `/capture` + `personal-untracked/inbox.md` — trusting capture over reacting; verb-first next-action language is already proactive by convention. |
| 2. Begin With the End in Mind | `personal-untracked/identity.md` (mission/roles) + each project's `info.md` "Desired Outcome" field — both already ask "what does done/this look like" before work starts. |
| 3. Put First Things First | `/daily`'s Top 3 Priorities, Energy Mapping, and time-blocking against `personal-untracked/calendar.md`'s skeleton. |
| 4. Think Win-Win | `personal-untracked/waiting-for.md` (commitments negotiated with others) + `/weekly`'s project-sync EDIT-block feedback loop, where outcomes get checked as still mutual. |
| 5. Seek First to Understand, Then to Be Understood | the `/slack` skill's triage/summarize/draft-reply flow, and `/weekly`'s EDIT-block feedback step — both listen before acting. |
| 6. Synergize | shared projects' `info.md`/`tasks.md`, `/weekly`'s project review section, and `personal-untracked/journal/` brain dumps (`/capture`, `/restart`) where combining ideas happens. |
| 7. Sharpen the Saw | `/weekly`'s own review cadence, `/daily`'s Energy Mapping, and `personal-untracked/calendar.md`'s recurring health/relationship/mind blocks — already a four-dimension renewal skeleton. |
| 8. Find Your Voice | `personal-untracked/identity.md`'s Mission section + mission-aligned projects (e.g. mentorship/teaching work), surfaced through Identity Calibration's keystone actions. |

## Cadence

Weekly review (`/weekly`) stays the primary touchpoint, extended over time with a "Habit
Calibration" section alongside the existing "Identity Calibration" once habit content exists to
calibrate against — see the Weekly Calibration Contract in `habits/README.md` for the
exact process that section will follow. The on-demand `/habit` command supplements this for
deliberate deep-dive sessions; `/onboard` only gives a light first exposure.

## Build vs. Practice — Two Different "Done"s

This distinction governs how the rest of the plan reads:

- **System build.** Whether a habit's phase (design, GTD integration, LLM-assisted path,
  calibration) is actually implemented is an engineering milestone. This governs when the
  *next* habit's phase begins being built — build order stays serial, per the sequencing above.
- **User mastery.** Per Covey's own upward-spiral model, a habit is never "complete" for the
  user, so it is never gated. Once a habit's system support exists it stays live indefinitely.
  See `habits/README.md` for how this reads to the user.

Do not conflate the two: a habit phase finishing its build means the mechanism works, not that
the user has "graduated" the habit.

## Current phase

**Phase B / Habit 1 (Be Proactive) build.** Foundation (Phase A) is complete: values alignment
via `personal-untracked/identity.md`, kept deliberately lightweight. `/onboard` drafts 5-8 short,
honest starter anchors, not a finished mission statement, plus a rough `## Roles` list and
one-sentence `## Mission` draft — something to open Habit 2 with, not the deliverable itself.
The deeper mission/roles pass is deferred until the user is actually working Habit 2 (Begin With
the End in Mind); that's Phase C's job, not Foundation's.

Foundation-path validation (B.5) is deliberately sequenced *after* Habit 1's own build (B.1-B.4),
not before: `/onboard` is meant to launch a new user straight into Habit 1, so validating the
whole path only makes sense once Habit 1 actually exists to onboard into. B.6 then validates
Habit 1's own path and weekly calibration specifically. Nothing beyond Habit 1 is being scoped
yet.
