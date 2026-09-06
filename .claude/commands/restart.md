# Restart

Open today's journal and guide a complete, **unstructured** brain dump of every open loop
in my head. The goal is to empty mental RAM onto the page — no organizing, no judging, no
fixing. Structure comes later (`/capture`, then the `/weekly` calibration). Right now we
just get it all out.

## Usage
```
/restart
```

## Behavior

1. Determine today's date (format `YYYY-MM-DD`).
2. Ensure the `journal/` folder exists; create it if it does not.
3. Open `journal/YYYY-MM-DD.md`. If it doesn't exist, create it seeded with:

   ```markdown
   # Journal - YYYY-MM-DD

   ## Notes

   ### Brain Dump on Open Loops

   ```

   If today's file already exists, append a new `### Brain Dump on Open Loops` section
   under `## Notes` rather than overwriting anything.

4. **Guide the dump, don't structure it.** Tell me plainly: write everything on my mind,
   in whatever order it arrives, however messy. No categories required, no full sentences
   required, no editing. Nothing is too small or too big. The only failure mode is leaving
   something in my head.

5. **Prime the pump with trigger prompts** so nothing hides. Offer these as nudges, not as
   a template to fill in — I free-write, you just make sure the corners get swept:
   - **Body & space** — health, sleep, substances, exercise, errands, the physical room
   - **Work** — current job, deadlines, blockers, things I'm avoiding
   - **My own thing** — startup / side projects, what's stalled, what needs to ship
   - **Admin & deadlines** — visa, money, appointments, anything with a date attached
   - **People** — relationships, conversations owed, people I'm out of sync with
   - **Mind & growth** — learning, reading, practice, who I'm trying to become
   - **Nagging unknowns** — anything that's been quietly bugging me with no home yet

6. **Stay out of the way while I write.** Capture what I say into the journal section
   verbatim — preserve my words, my phrasing, my mess. Do **not** rewrite, summarize,
   prioritize, or turn loops into tasks during the dump. If I trail off, ask only: *"What
   else is still in there?"* and keep going until I say I'm empty.

7. When I signal I'm done, confirm the dump is saved and report the journal path. Then
   offer — but do not auto-run — the next steps:
   - `/capture` — pull concrete next actions out of the loops
   - `/daily` — plan the day around them
   - `/weekly` — when it's review time, calibrate present self against `personal-untracked/identity.md`

   The dump itself stays raw. That's the point.
