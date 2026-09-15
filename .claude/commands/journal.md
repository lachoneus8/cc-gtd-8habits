# Journal

Create a new journal entry file for today.

## Usage
```
/journal
```

## Behavior
1. Determine today's date (format `YYYY-MM-DD`).
2. Ensure the `personal-untracked/journal/` folder exists in the working directory; create it if
   it does not.
3. Create a new file at `personal-untracked/journal/YYYY-MM-DD.md`.
   - If a file for today already exists, open it instead of overwriting.
4. Seed the new file with a simple template:

```markdown
# Journal - YYYY-MM-DD

> Private: this file is private user context for Claude Code. Keep it in `personal-untracked/`;
> do not move its contents into tracked repository guidance.

## Notes

```

5. Report the path of the file that was created or opened.
