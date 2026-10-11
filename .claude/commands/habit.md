# Habit

On-demand deep-dive session on a specific habit — revisit its core idea, sit with its reflection
prompts, decide on practice, log what happened. The lighter counterparts are `/onboard`'s first
touch and `/weekly`'s recurring Habit Calibration; this is for when you want to actually spend
time with a habit. See `habits/README.md` for how this fits the rest of the system.

## Usage

```
/habit [habit name or number]
```

## Behavior

### 1. Pick the habit

- If an argument names a habit, use it if `habits/habit<N>.md` exists for it.
- Otherwise, read `personal-untracked/habits.md`'s Current Focus. If it names a habit with
  content under `habits/`, use that.
- Otherwise, ask which habit to work on — list only habits that actually have content under
  `habits/` (right now, Habit 1: Be Proactive and Habit 2: Begin With the End in Mind). Never assume; Current Focus is self-declared
  and this command does not set it on your behalf (see step 4).
- If no habit has content under `habits/` yet, say so plainly and stop — there's nothing to run
  a session on.

### 2. Start the habit if it's new

If the chosen habit isn't yet in `personal-untracked/habits.md`'s Started Habits, confirm before
adding it — "Start Habit N now?" — then append (using that habit's number and name, e.g.
`### Habit 1 — Be Proactive`):

```markdown
### Habit N — <Name>

**Started:** YYYY-MM-DD

**Practice Log**
```

Skip this step if the habit is already started; go straight to the session.

### 3. Run the session

Read `habits/habit<N>.md`'s **Habit Content** section (Principle, Reflection Prompts, Practice,
and any Guardrails for the LLM) — never its Research section, which is background for design
work, not something to recite to the user. Any Guardrails for the LLM in that section bind this
session.

For Habit 2, also read `personal-untracked/identity.md` (Roles and Mission) first so the
conversation starts from the user's own words. Habit 2's "Going deeper" options are where the
real work happens; offer one per session. Roles and Mission text is written to `identity.md`
only on the user's explicit instruction in this session, in their words — never drafted or
polished for them — and that write is separate from, and in addition to, the Practice Log line
in step 4.

- Open with the Principle in your own words — brief, not a lecture.
- Work through a couple of Reflection Prompts conversationally. Pick what fits where the
  conversation actually goes; don't march through the full list like a form.
- Land on Practice: confirm one of the default practices, or — only if there's time and
  appetite — one of the "Going Deeper" options.

### 4. Log it, don't invent it

Append one dated line to that habit's Practice Log in `personal-untracked/habits.md`,
summarizing what actually came up and what they're committing to practice — in their own words
where it matters, not a transcript. Log the practice as they actually phrased or adapted it in
this session, not the habit file's stock wording of it. If they didn't commit to anything specific, log
that no practice was agreed rather than adding one. Never fabricate progress, commitments, or
backdate entries.

Then, separately, ask whether to set this habit as Current Focus if it isn't already — write
`personal-untracked/habits.md`'s Current Focus only on an explicit yes this session. Starting a
habit and making it Current Focus are two different decisions; don't conflate them.

### 5. Close

Name what's next in one line: this session's practice log feeds `/weekly`'s Habit Calibration
automatically — no separate action needed.

## Guardrails

- Never invent, embellish, or backdate Practice Log entries.
- Never write Current Focus without an explicit yes given this session.
- Don't close with praise or an evaluation of how the session went; a plain one-line close is
  enough (see the Voice section in `habits/README.md`).
- Don't force every Reflection Prompt or both Practice items — this is a conversation, not a
  checklist (see the Voice section in `habits/README.md`).
- If no habit has content yet under `habits/`, say so and stop rather than improvising content
  that isn't there.
- For Habit 2: never author, suggest wholesale, or "improve" Roles or Mission text unprompted.
