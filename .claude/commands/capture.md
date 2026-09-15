# Capture

Quickly capture thoughts, ideas, and tasks. Uses AI to auto-process obvious single-step actions.

## Usage

```
/capture [item]
```

## Smart Processing

The command automatically processes items when they are:

- **Clear single actions** with obvious context
- **Complete information** (no ambiguity about what to do)
- **Actionable immediately** (not research or multi-step projects)

Auto-processed items are simultaneously:

1. Added to the appropriate project's `tasks.md` file in GTD system
2. Created in the corresponding Todoist project (via the Todoist MCP server) with the proper `@context` label

## Examples

**Auto-processed (goes directly to project tasks):**

```
/capture "Call dentist to schedule cleaning"
→ Personal health project: @home-calls: Call dentist to schedule cleaning

/capture "Email teammate about Friday meeting agenda"
→ Relevant work project: @work-computer: Email teammate about Friday meeting agenda

/capture "Buy milk on way home"
→ General tasks: @errands: Buy milk on way home
```

**Sent to inbox (needs clarification):**

```
/capture "Research new project management tools"
→ personal-untracked/inbox.md (unclear scope, needs processing)

/capture "Team meeting went badly"
→ personal-untracked/inbox.md (unclear what action to take)

/capture "Fix the website issue"
→ personal-untracked/inbox.md (vague, needs more specifics)
```

## AI Analysis

For each captured item, analyzes:

- **Clarity**: Is the action specific and unambiguous?
- **Context**: Can we determine the appropriate @context?
- **Project**: Does this belong to an existing active project?
- **Completeness**: Is all necessary information present?
- **Actionability**: Is it a single physical action?

Tasks are added to the appropriate project's `tasks.md` file under the correct context section and simultaneously created in the corresponding Todoist project (via the Todoist MCP server) with the proper `@context` label.

## Habit 1 Integration (Be Proactive)

Check `personal-untracked/habits.md`'s Started Habits first. If Habit 1 isn't there, skip this
section entirely — capture behaves exactly as documented above, unmodified. GTD works standalone
regardless of habit progress.

If Habit 1 is started:

- **Actionability *is* the Circle of Influence question.** GTD's own "is this actionable?" test
  and Habit 1's Circle of Influence/Concern sort are the same question asked two ways. When
  something can't get a concrete next action because it's genuinely not this person's to act on
  right now, say so plainly instead of quietly parking it — e.g. "this isn't something you can
  act on right now, not that it's unimportant" rather than a bare inbox entry with no comment.
  Still park it exactly where it would otherwise go (inbox, someday-maybe, waiting-for); this is
  about naming *why*, not changing the routing.
- **Write next actions in proactive language on purpose, not by accident.** GTD's verb-first
  convention already trends this way — with Habit 1 active, be deliberate about it: prefer
  ownership phrasing ("Decide whether to...", "Reply to X about Y") over vague reactive framing
  ("Deal with X", "Handle the Y situation").
- **Notice a pattern, don't just process the instance.** If the same unresolved item keeps
  resurfacing across captures without ever getting a real next action, that's worth naming as a
  possible Circle-of-Concern item the next time it comes up, rather than reprocessing it the same
  way indefinitely.

## Todoist Integration

When auto-processing tasks, the system:

1. **Identifies the target project** from active GTD projects
2. **Maps GTD context to a Todoist label** (`@work-code`, `@work-errand`, `@home-computer`, etc.)
3. **Creates the task** in the matching Todoist project with content `[Task]`, label `@context` (plus priority/due date if known)
4. **Handles inbox items** by creating them in the Todoist `Inbox` project for later processing

If no clear project exists, items go to both GTD personal-untracked/inbox.md and the Todoist `Inbox` project for processing.

## Fallback Behavior

When in doubt, items go to personal-untracked/inbox.md with timestamp and the Todoist `Inbox` project:

- **GTD**: `- [ ] YYYY-MM-DD HH:MM - [item]` in personal-untracked/inbox.md
- **Todoist**: Created in the `Inbox` project with content `[item]`

## Implementation Notes

- **Duplicate prevention**: Check if a similar task already exists before creating
- **Context mapping**: Use a consistent GTD context → Todoist label mapping
- **Priority assignment**: Default to p4 (normal), higher for urgent keywords
- **Due dates**: Set the Todoist `due` date when the item implies one
- **Error handling**: If Todoist creation fails, still add to GTD system
- **Sync consistency**: Maintain bidirectional sync between GTD and Todoist
