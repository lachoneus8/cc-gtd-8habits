# Slack Usage Notes for GTD Integration

## Access Methods

Use the least invasive method that can answer the request:

1. User-provided transcript, screenshot text, or Slack permalink.
2. Browser/Chrome access to the user's logged-in Slack workspace.
3. Slack export files, usually JSON files grouped by channel and date.
4. Slack Web API, only if `SLACK_BOT_TOKEN` or an equivalent credential is already configured.

Do not request or print Slack tokens. If API access is unavailable, ask for a permalink, copied thread, export file, or permission to use the browser.

## Useful Slack API Calls

These examples assume a bot/user token is already configured as `SLACK_BOT_TOKEN`.

### Test Authentication

```bash
curl -sS -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  https://slack.com/api/auth.test
```

### List Channels

```bash
curl -sS -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  "https://slack.com/api/conversations.list?types=public_channel,private_channel,mpim,im&limit=200"
```

### Fetch Channel History

```bash
curl -sS -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  "https://slack.com/api/conversations.history?channel=$CHANNEL_ID&limit=100"
```

### Fetch Thread Replies

```bash
curl -sS -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  "https://slack.com/api/conversations.replies?channel=$CHANNEL_ID&ts=$THREAD_TS"
```

### Search Messages

```bash
curl -sS -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  --get https://slack.com/api/search.messages \
  --data-urlencode "query=from:me after:YYYY-MM-DD has:link" \
  --data-urlencode "count=20"
```

## GTD Triage Rules

- Treat mentions, direct asks, and explicit owners as likely next actions.
- Treat "I'll", "can you", "please", "by Friday", "waiting on", "blocked by", and "ship/review/approve/follow up" as high-signal phrases.
- Capture unclear asks as clarifying follow-ups rather than inventing scope.
- Put delegated work in `personal-untracked/waiting-for.md` with owner, expected outcome, date, and source link.
- Put time-specific items in `personal-untracked/calendar.md` or the relevant daily note.
- Put project-specific actions in `projects/active/<project>/tasks.md` under the closest context.
- Preserve Slack permalinks when available; otherwise include channel, author, and timestamp.

## Search Query Patterns

Useful Slack search terms:

```text
from:me "I'll"
to:me "can you"
to:me "please"
"waiting on" OR "blocked"
"by Friday" OR "EOD" OR "tomorrow"
has:link after:YYYY-MM-DD
in:channel-name after:YYYY-MM-DD before:YYYY-MM-DD
```

When searching from browser UI, prefer narrow date/channel/person filters before broad keyword searches.

## Reply Drafting

Slack replies should be concise and concrete:

- Confirm what will happen next.
- Name owner and date when possible.
- Ask one clarifying question if the request is ambiguous.
- Avoid over-explaining GTD processing in the reply.
