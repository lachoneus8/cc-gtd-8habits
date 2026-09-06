# Onboard

Guide a new user from a freshly cloned repo to a working first GTD loop.

Assume the user already has Claude Code set up and is running this command from the repo
root. Do not assume Todoist, Google Calendar, or Slack are connected; integrations are
optional and should not block the first local workflow.

## Usage
```
/onboard
```

## Goal

Get the user to a trustworthy first daily loop:

1. Private workspace exists.
2. Identity anchors are drafted.
3. Active project map exists.
4. First project files exist.
5. Calendar skeleton exists.
6. A raw brain dump is captured.
7. Obvious actions are processed.
8. Today's `personal-untracked/todo.md` is created.
9. User knows the evening and weekly follow-up commands.

## Behavior

Proceed as an interactive wizard. Keep momentum. Prefer lightweight defaults over asking
for perfect answers. When the user is unsure, create a reasonable starter version and mark
it for later refinement.

### 1. Initialize the Workspace

First, check whether the private workspace files exist:

- `personal-untracked/identity.md`
- `personal-untracked/projects.md`
- `personal-untracked/calendar.md`
- `personal-untracked/inbox.md`
- `personal-untracked/waiting-for.md`
- `personal-untracked/someday-maybe.md`
- `daily/`
- `journal/`
- `projects/active/`
- `projects/archived/`
- `reviews/`
- `weekly/`

If any are missing, run `just setup` if available. If `just` is unavailable, create the
same files/directories from `templates/` manually.

Do not overwrite existing private files.

Then verify privacy:

- Confirm `.gitignore` ignores the `personal-untracked/` folder and private runtime folders.
- If a private file is not ignored, warn the user and fix `.gitignore` before continuing.

### 2. Explain the System in One Minute

Give the user the mental model:

- `journal/` is raw thinking.
- `personal-untracked/inbox.md` is unprocessed capture.
- `projects/active/*/info.md` holds outcomes and status.
- `projects/active/*/tasks.md` holds next actions by context.
- `personal-untracked/calendar.md` mirrors fixed commitments and recurring blocks.
- `personal-untracked/todo.md` is only today's working list.
- `daily/` records the plan, work log, and reflection.
- `weekly/` keeps the system honest.

Then explain the operating loop:

```text
/restart -> /capture -> /daily -> personal-untracked/todo.md during the day -> /shutdown -> /weekly
```

### 3. Draft Identity Anchors

Open `personal-untracked/identity.md`. If it still looks like the template, ask the user for 5-8 identity
anchors. Keep prompts concrete:

- Mornings / energy
- Body and space
- Work
- Creative or personal projects
- Relationships
- Mind / learning
- Attention / inputs
- Life rhythm

Write concise first-person statements. Do not make them grandiose. These are durable
directional anchors, not goals.

If the user wants to skip this, keep the template and add a short TODO at the top:

```markdown
> TODO: Replace these starter anchors after the first weekly review.
```

### 4. Build the First Project Map

Open `personal-untracked/projects.md`. If it still looks like the template, suggest this starter set:

- `work`
- `health-and-foundation`
- `admin`
- `relationships`
- `personal-projects`
- `learning`

Ask the user to confirm, rename, remove, or add projects. Keep the first pass to 4-8 active
projects.

For each confirmed project:

1. Normalize the folder name to lowercase kebab-case.
2. Run `just add-project <folder-name>` if available, or create files from templates.
3. Fill `info.md` with:
   - desired outcome
   - current status
   - constraints/deadlines, if known
4. Leave `tasks.md` with context headings.

Update `personal-untracked/projects.md` Active Projects with the chosen names and one-line outcomes.

If Todoist is connected, add a minimal sync map only after local projects are clear. If it
is not connected, leave Todoist IDs blank and note that `/todoist` can fill them later.

### 5. Create the Calendar Skeleton

Open `personal-untracked/calendar.md`. If it still looks like the template, guide the user to create a normal
weekday skeleton. Ask for rough blocks, not perfect scheduling:

- wake / morning routine
- commute or transition time
- work / school
- meals
- exercise
- relationship / family / social time
- creative / personal project time
- shutdown / reading / sleep

Also capture hard dated commitments in `## Time-Specific Items`.

If Google Calendar is connected, offer to run `/calendar` after onboarding to sync real
events. Do not require it.

### 6. Capture the First Brain Dump

Create or open today's `journal/YYYY-MM-DD.md`. Add:

```markdown
### Onboarding Brain Dump
```

Guide an unstructured dump. Use trigger prompts, but do not turn this into a form:

- What is on your mind right now?
- What are you responsible for this week?
- What is late, blocked, or nagging?
- Who are you waiting on?
- Who is waiting on you?
- What decisions are unresolved?
- What dates or deadlines matter?
- What would feel relieving to have written down?

Capture the user's words verbatim. Do not organize while dumping.

### 7. Process Only the Obvious

After the dump, process only clear items:

- clear next actions -> relevant `projects/active/<project>/tasks.md`
- delegated items -> `personal-untracked/waiting-for.md`
- hard dates -> `personal-untracked/calendar.md`
- future/maybe ideas -> `personal-untracked/someday-maybe.md`
- unclear items -> `personal-untracked/inbox.md`

Use GTD next-action language: verb first, concrete, small enough to do.

Do not over-process vague thoughts. The onboarding win is trust, not completeness.

If Todoist is connected, create matching tasks through `/todoist` or Todoist MCP. If not,
leave them local.

### 8. Make the First Daily Plan

Create today's `daily/YYYY-MM-DD.md` and `personal-untracked/todo.md`.

Daily log structure:

```markdown
# Daily Log - YYYY-MM-DD

## Daily Plan
**Last Updated:** HH:MM

### Top 3 Priorities
1. [ ] ...
2. [ ] ...
3. [ ] ...

### Time Blocks
- ...

### Energy Mapping
- High:
- Medium:
- Low:

## Work Log
<!-- Fill in at /shutdown -->

## Reflection
<!-- Fill in at /shutdown -->
```

`personal-untracked/todo.md` structure:

```markdown
# Todo - YYYY-MM-DD

## Top 3
- [ ] ... (Project)

## Today
- [ ] ... (Project)

## Captured
<!-- jot new tasks/loops here during the day; /shutdown processes them -->
```

Pick a realistic Top 3. If the user has too many tasks, explicitly defer most of them.

### 9. Finish With the Operating Instructions

End by showing the user exactly what to do next:

- During the day: work from `personal-untracked/todo.md`; add new loops under `## Captured`.
- Tonight: run `/shutdown`.
- Tomorrow morning: run `/daily`.
- End of week: run `/weekly`.
- Anytime overwhelmed: run `/restart`.
- Anytime a message/thread needs action triage: run `/slack`.

Also remind them:

- Personal files are intentionally ignored by git.
- MCP integrations are optional; local markdown works first.
- The system gets better after the first shutdown and first weekly review.

## Guardrails

- Do not ask for secrets or tokens.
- Do not commit or stage files.
- Do not overwrite existing private files.
- Do not create more than 8 active projects in onboarding unless the user insists.
- Do not run `/shutdown` or `/weekly` automatically during onboarding.
- Keep the user moving; leave TODOs for refinements that are not needed for today's loop.
