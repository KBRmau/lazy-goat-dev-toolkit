# Weekly recap

What happened this ISO week (Monday 00:00 local through now, or through Sunday if the week is over). Portuguese unless the team thread is English. Humanizer. Facts only. No rewrite of session notes: link them.

## Trigger

`/auto-work weekly` or `semana`. Optional `last` / `passada` for the previous full ISO week. Do not treat this as an inbox tick: do not start P3 implementation.

## Window

- Default: current ISO week, Monday 00:00 local → now.
- `last`: previous Monday 00:00 → that Sunday 23:59 local.
- Filename uses ISO week: `YYYY-Www` (example `2026-W39`).

## Sources (skip missing)

1. Vault: `digest/*-standup.md`, `digest/*-briefing.md`, `digest/YYYY-MM-DD.md`, `meetings/` whose dates fall in the window. Link them. Do not paraphrase bodies.
2. Jira: `assignee = currentUser() AND updated >= startOfWeek() ORDER BY updated DESC` (limit 20). For `last`, use the previous week's Monday date in JQL (`updated >= "YYYY-MM-DD" AND updated <= "YYYY-MM-DD"`).
3. GitHub: PRs you authored that merged in the window (`gh search prs --author=@me --merged --merged-at <start>..<end>`). Open PRs that sat the whole week with no review also go under Ruins if that is true.
4. Slack: only facts already in vault digest/briefing or a thread the user pasted. Do not send.
5. Granola: titles in `<vault>/meetings/` for the window.

Do not invent metrics, comments, or merges. If a source is missing, say so in one line.

## Output (chat + vault)

Write `<vault>/digest/YYYY-Www-weekly.md` with exactly these headings:

```
# Weekly YYYY-Www (YYYY-MM-DD -> YYYY-MM-DD)

## Feito
## Bons
## Ruins
## Ainda aberto
## Fontes
```

**Feito:** bullets of work that landed or moved in the window. Ticket keys and PR numbers. One fact per bullet.

**Bons:** what went well (merge, unblock, measurement, decision). Only items with evidence in Feito or Fontes.

**Ruins:** slips, waits, dropped messages, red CI, reviews that did not come, tools that were down. Same evidence rule.

**Ainda aberto:** tickets and PRs still blocking next week. Next action in one clause.

**Fontes:** links to standup/briefing/meetings in the vault. No body rewrite.

Do not commit this file into the current project git. It stays in `<vault>/digest/`.
