setup:
    @mkdir -p daily/ journal/ projects/active projects/archived reviews/ weekly/ personal-untracked/
    @[ -e personal-untracked/inbox.md ] || cp templates/inbox.md personal-untracked/inbox.md
    @[ -e personal-untracked/projects.md ] || cp templates/projects.md personal-untracked/projects.md
    @[ -e personal-untracked/waiting-for.md ] || cp templates/waiting-for.md personal-untracked/waiting-for.md
    @[ -e personal-untracked/someday-maybe.md ] || cp templates/someday-maybe.md personal-untracked/someday-maybe.md
    @[ -e personal-untracked/calendar.md ] || cp templates/calendar.md personal-untracked/calendar.md
    @[ -e personal-untracked/identity.md ] || cp templates/identity.md personal-untracked/identity.md

add-project project:
    @mkdir -p projects/active/{{project}}
    @[ -e projects/active/{{project}}/info.md ] || cp templates/project-info.md projects/active/{{project}}/info.md
    @[ -e projects/active/{{project}}/tasks.md ] || cp templates/project-tasks.md projects/active/{{project}}/tasks.md

onboard:
    @echo "1. Run: just setup"
    @echo "2. In Claude Code, run: /onboard"
    @echo "3. Use ONBOARDING.md as the written reference"
