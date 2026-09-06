# Shutdown

The end-of-day ritual (pairs with the scheduled **Shutdown** calendar block). Walk today's
`personal-untracked/todo.md`, close the loops, record what got done onto today's daily log, decide tomorrow's
shape, then help me empty my head so I can stop thinking about work and go about my evening.

`/daily` plans the day and creates `personal-untracked/todo.md`; I update it all day; `/shutdown`
reconciles it at night. Counterpart to `/daily`.

## Usage
```
/shutdown
```

## Behavior

### 1. Read today's state
- Read `personal-untracked/todo.md` and today's `daily/YYYY-MM-DD.md`.
- Invoke the `/todoist` skill first if Todoist may be out of sync.

### 2. Close the loops (what got done)
- For each **checked** `[x]` item in `personal-untracked/todo.md`:
  - Mark it complete in the matching project `projects/active/<project>/tasks.md`
    (`- [ ]` → `- [x]`), using the `(Project)` tag on the line to route it.
  - Complete the corresponding **Todoist** task (find by content in that project; use
    `complete-tasks`). Never auto-complete anything that isn't checked in `personal-untracked/todo.md`.
  - Log it in today's daily `## 📝 Work Log`.
- For each item in `personal-untracked/todo.md`'s `## Captured` section: process like `/capture` — route real
  next-actions to the right project `tasks.md` + Todoist (with `@context`), and anything
  vague to the inbox/journal. Don't lose anything.

### 3. Record the day onto the daily log
- Fill today's `## 📝 Work Log` (what happened) and `## 🔄 Reflection` (wins, what slipped
  and why, adjustments). Be honest and specific — this is the same reflection `/weekly`
  reads later. Infer what got done from `personal-untracked/todo.md` + completions; if a Top-3 didn't land,
  say so and why.

### 4. Decide tomorrow
- Carry every **unchecked** `personal-untracked/todo.md` item forward (leave it open in its project/Todoist so
  tomorrow's `/daily` repulls it). Reschedule due dates if needed via `reschedule-tasks`.
- Glance at tomorrow's calendar (`/calendar`) for fixed commitments and deadline pressure.
- Write a short **"Tomorrow's focus"** line into today's Reflection (the 1–3 things that
  matter most). Don't build tomorrow's full plan — that's tomorrow's `/daily`.

### 5. Empty my head (open loops)
- Run a quick brain-sweep like a light `/restart`: ask what's still rattling around —
  work, personal, nagging unknowns. Capture verbatim into today's journal
  (`journal/YYYY-MM-DD.md`, under `## Notes`) or route clear actions as in step 2.
- Keep asking *"what else is still in there?"* until I'm empty. The goal is nothing left in
  my head to think about tonight.

### 6. Confirm shutdown
- Report: loops closed (n), carried to tomorrow (n), captured (n), tomorrow's focus.
- Confirm `personal-untracked/todo.md` is reconciled and the day is logged. Then I'm done — go about the evening.
