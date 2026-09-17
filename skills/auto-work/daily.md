# Daily briefing (07:00)

Standup script. Portuguese unless the team speaks English. Humanizer. About 45–60 seconds spoken. No rewrite of session notes: link them.

## Trigger

`/auto-work daily` or the 07:00 weekday loop. Do not treat this as an inbox tick: do not start P3 implementation.

## Sources (skip missing)

1. `python ~/.cursor/skills/auto-work/scripts/daily_digest.py` then read that file.
2. Jira: `assignee = currentUser() AND status not in (Done, Closed, Canceled) ORDER BY updated DESC` (limit 10).
3. GitHub this repo: open PRs by you, human review comments on those PRs, failing checks. Do not turn CODEOWNERS review-requested on other PRs into standup work.
4. Slack: skip until MCP tools are listed and authenticated. If the user pasted a thread, one line.
5. Granola/meetings: titles from `meetings/` in the last 24h only.

## Output (chat + vault)

Write `<vault>/digest/YYYY-MM-DD-standup.md` with exactly these headings:

```
# Standup YYYY-MM-DD

## Fala (ontem / hoje / bloqueio)

## Inbox
## Sessoes 24h
```

**Fala:** three short spoken blocks. Facts only. Ticket keys. No padding.

**Inbox:** PRs and Jira keys, status, next action. No Jira/GitHub writes.

**Sessoes 24h:** bullets that link digest entries. Do not paraphrase bodies.

Do not commit this file into the current project git. It stays in `<vault>/digest/`.
