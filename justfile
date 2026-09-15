setup:
    @mkdir -p personal-untracked/daily personal-untracked/journal personal-untracked/projects/active personal-untracked/projects/archived personal-untracked/reviews personal-untracked/weekly
    @[ -e personal-untracked/inbox.md ] || cp templates/inbox.md personal-untracked/inbox.md
    @[ -e personal-untracked/projects.md ] || cp templates/projects.md personal-untracked/projects.md
    @[ -e personal-untracked/waiting-for.md ] || cp templates/waiting-for.md personal-untracked/waiting-for.md
    @[ -e personal-untracked/someday-maybe.md ] || cp templates/someday-maybe.md personal-untracked/someday-maybe.md
    @[ -e personal-untracked/calendar.md ] || cp templates/calendar.md personal-untracked/calendar.md
    @[ -e personal-untracked/identity.md ] || cp templates/identity.md personal-untracked/identity.md
    @[ -e personal-untracked/habits.md ] || cp templates/habits.md personal-untracked/habits.md

add-project project:
    @mkdir -p personal-untracked/projects/active/{{project}}
    @[ -e personal-untracked/projects/active/{{project}}/info.md ] || cp templates/project-info.md personal-untracked/projects/active/{{project}}/info.md
    @[ -e personal-untracked/projects/active/{{project}}/tasks.md ] || cp templates/project-tasks.md personal-untracked/projects/active/{{project}}/tasks.md

onboard:
    @echo "1. Run: just setup"
    @echo "2. In Claude Code, run: /onboard"
    @echo "3. Use ONBOARDING.md as the written reference"
