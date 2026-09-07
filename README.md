# 7 Habits + GTD with Claude Code

A Getting Things Done (GTD) implementation with Claude Code powered task processing and daily
planning, extended with Stephen Covey's 7 Habits (and the later 8th Habit) as the values
foundation underneath it.

**This is a fork of [adagradschool/cc-gtd](https://github.com/adagradschool/cc-gtd).** Full
credit for the original GTD system design and implementation goes to that project and its
author. This fork keeps that GTD engine intact and layers Covey's habits on top as the "why"
behind the system, so the discipline has something to anchor to beyond the mechanics.

**New here? Run `/onboard`.** It guides the first setup, brain dump, project map, daily
plan, and next habits. [ONBOARDING.md](ONBOARDING.md) is the written reference.

## Overview

This system implements David Allen's GTD methodology with modern AI enhancements for:

- Smart task capture and processing
- Automated project organization
- Daily planning and work logging
- Integration with external tools through MCP (Todoist, Google Calendar)

## Features

### Core GTD Implementation

- **Inbox** for quick capture with timestamps
- **Projects** with dedicated tracking and task management
- **Contexts** for organizing next actions by location/tool
- **Waiting For** list for delegated items
- **Someday/Maybe** for future possibilities
- **Reference** materials organization

### AI Enhancements

- Smart capture that auto-processes obvious actions
- Intelligent processing that skips unnecessary GTD steps
- Daily planning assistance
- External tool synchronization

## File Structure

```
gtd/
├── personal-untracked/         # User-specific files, ignored as one folder
│   ├── inbox.md                # Raw capture with timestamps
│   ├── projects.md             # Project dashboard (read-only overview)
│   ├── waiting-for.md           # Delegated/expected items
│   ├── someday-maybe.md         # Future possibilities
│   └── calendar.md              # Time-specific items
├── projects/active/            # Active projects
│   └── [project-name]/
│       ├── info.md             # Project goals, outcomes, progress
│       └── tasks.md            # Context-organized next actions
├── projects/archived/          # Completed projects
├── reviews/weekly-review.md    # Review templates
├── daily/YYYY-MM-DD.md         # Daily planning and work logs
└── reference/                  # Non-actionable materials
```

## Commands

- `/capture [item]` - Smart capture with auto-processing
- `/daily` - Plan for the day
- `/todoist` - Sync with Todoist through the Todoist MCP server
- `/calendar` - Pull Google Calendar context through the Google Calendar MCP server
- `/weekly` - Conduct weekly review
- `/onboard` - Guided first-run setup and GTD onboarding
- `/restart` - Restart the day from current context
- `/shutdown` - End-of-day reconciliation
- `/journal` - Capture a journal entry

## Context System

Organize tasks by context for efficient execution:

- `@work-code` - Coding tasks (work)
- `@work-errand` - Work-related errands
- `@home-computer` - Personal computer tasks
- `@home-calls` - Personal phone calls
- `@sideprojects-code` - Side project coding
- `@sideprojects-errand` - Side project errands
- `@mobile-anywhere` - Mobile tasks
- `@errands` - Out-of-home tasks
- `@agenda-[person]` - Person-specific items

## Project Management

Each active project contains:

- **info.md**: Goals, desired outcomes, progress tracking, history
- **tasks.md**: Next actions organized by context

Projects move to `archived/` upon completion with proper status documentation.

## Daily Planning

Daily files (`daily/YYYY-MM-DD.md`) include:

- **Daily Plan**: Priorities, time blocks, energy mapping
- **Work Log**: Timestamped activities with durations
- **Reflection**: What worked, improvements, next day focus

## Setup & Installation

### Prerequisites

1. **Claude Code** - The AI assistant that powers this system
2. **Just** - Command runner for project automation
   - Install: `cargo install just`
   - Documentation: [https://github.com/casey/just](https://github.com/casey/just)
3. **Todoist MCP server** - Configured in `.mcp.json`
4. **Google Calendar MCP server** - Required for `/calendar`, `/daily`, and `/weekly`

### Installation Steps

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd gtd
   ```

2. Run the setup command:

   ```bash
   just setup
   ```

3. In Claude Code, run:

   ```text
   /onboard
   ```

4. Confirm the MCP servers are connected in Claude Code, if using integrations:
   - Todoist: `.mcp.json` points to `https://ai.todoist.net/mcp`
   - Google Calendar: connect the calendar MCP server for `/calendar`

5. Start capturing tasks with `/capture`!

### Additional Commands

The `justfile` includes helpful commands:

- `just setup` - Creates private local files from templates without overwriting existing data
- `just onboard` - Prints the first-run command sequence
- `just add-project project-name` - Creates a new project with info.md and tasks.md

## Privacy

The repo is designed to share commands, skills, and templates while keeping personal data
local. The default `.gitignore` excludes the `personal-untracked/` folder, private runtime
folders, and local MCP config.

## Smart Processing Logic

The AI assistant intelligently processes captures:

- **Auto-processes**: Clear, single actions with obvious context
- **Sends to inbox**: Vague items, multi-step projects, unclear scope

During processing, it skips obvious steps:

- Already defined items skip "What is it?"
- Action verbs skip "Is it actionable?"
- Specific actions skip "Next action?"
- Complex tasks skip "<2 minutes?"

## Best Practices

1. **Capture everything** - Use the inbox liberally
2. **Process regularly** - Keep inbox at zero
3. **Review weekly** - Maintain system integrity
4. **One task, one place** - No duplication across files
5. **Update progress** - Keep project info current

## Energy Management

The system supports energy-based planning:

- Track energy levels in daily planning
- Map tasks to appropriate energy states
- Review energy patterns in weekly reviews

## Integration

Designed to work with:

- Todoist MCP for task sync and mobile capture
- Google Calendar MCP for schedule context and time blocking
- AI assistants for processing automation

## License

This GTD system structure is open source and available for anyone to use and adapt for their personal productivity needs.

## Credits

- **GTD system design & implementation:** [adagradschool/cc-gtd](https://github.com/adagradschool/cc-gtd)
  on GitHub — this fork's inbox/projects/contexts/reviews/daily-planning engine, commands, and
  private/shareable file split are theirs. All credit for that work belongs to them.
- **GTD methodology:** David Allen's _Getting Things Done_.
- **Habits layer:** Stephen Covey's _The 7 Habits of Highly Effective People_ (30th Anniversary
  Edition) and _The 8th Habit_, adapted here as the identity/mission foundation underneath the
  GTD loop above.
