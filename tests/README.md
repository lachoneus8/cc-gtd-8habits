# Automated Validation Harness

Runs a scripted, LLM-driven conversation against the real command files and grades it — so a
habit's `.5` validation step doesn't depend on anyone's private `personal-untracked/` content.

```
just test-scenario habit2-session
# or: python tests/harness/run_scenario.py <scenario> [--max-turns N] [--keep] [--budget USD]
```

Requires the `claude` CLI, `git`, and Python 3. Each run makes real API calls (agent, simulated
user, evaluator). Exit code is non-zero if any check or rubric item fails.

## How a run works

1. **Sandbox.** Copies the tracked repo content (`.claude/` minus settings, `templates/`,
   `habits/`, `context/`, top-level docs) into a temp directory and drops the scenario's
   `fixture/` in as `personal-untracked/`. Your real `personal-untracked/` is never read or
   written. The sandbox is `git init`-ed so the exact changes the agent made can be diffed.
2. **Agent under test.** `claude -p` in the sandbox, project settings only, edit tools only (no
   web, no MCP). It starts from the scenario's `opening_prompt` (a real slash command) and
   continues over `--resume`. It is told Todoist/Calendar/Slack are unavailable and to skip them.
3. **Simulated user.** A separate tool-less `claude -p` call per turn, given only the persona
   and the transcript — it cannot see the repo or the rubric. It ends the session with `[END]`.
4. **Grading.**
   - *Deterministic checks* from `scenario.json` (file changed/unchanged, pattern present, only
     expected files touched, privacy note on new private files).
   - *Evaluator*: a tool-less `claude -p` call that scores each `rubric.md` item pass / fail / n/a
     with a quoted evidence line, given the transcript, the diff, and the deterministic results.

Output lands in `tests/runs/<scenario>-<timestamp>/` (gitignored): `transcript.md`,
`changes.diff`, `report.json`.

## Adding a scenario

Create `tests/scenarios/<name>/` with:

- `fixture/` — a **fictional** persona's `personal-untracked/` tree. Never copy real user
  content here; this directory is tracked. Keep the privacy note on every file.
- `persona.md` — who the simulated user is, and how they behave (including any deliberate
  baiting, e.g. asking the assistant to write their mission for them).
- `rubric.md` — bullet items `**id** — what good looks like`, drawn from the habit's Calibration
  Criteria and Guardrails. Mark when an item can legitimately be n/a.
- `scenario.json` — `opening_prompt`, `max_turns`, optional `today`, and `checks`. Check types:
  `file_contains`, `file_not_contains`, `file_changed`, `file_unchanged`, `only_changed`
  (globs), `privacy_header_on_new`.

## Caveats

- LLM runs are non-deterministic: treat a single rubric failure as a flag to read the transcript,
  and re-run before concluding a command regressed. Deterministic checks are the firm signal.
- Integrations (Todoist, Calendar, Slack) are out of scope; this exercises the habit layer and the
  local-file GTD behavior only.
- Simulated-user personas are prompts, not real users — they complement one genuine run by the
  person the system is for, they don't replace it.
