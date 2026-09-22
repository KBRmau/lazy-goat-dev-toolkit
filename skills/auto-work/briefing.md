# Briefing tick (loop)

Default for `/loop 15m /auto-work briefing`. Status board, not one-item inbox.

## Trigger

Loop prompt contains `briefing`, `status`, or the armed 15m briefing loop. `/auto-work` without those words still runs the one-item inbox tick (`SKILL.md`).

## Do (every tick)

Scan all of the following. Do not stop at the first hit. Do not spawn a P3 worker. Do not skip a ticket because it is in `last_ids` or `blocked`.

1. **Tracked tickets** in state `tickets:` (keys the user listed). For each: Jira status, last comment author/time, blocker, what changed since the previous tick.
2. **Slack** per `slack.md`: unreads, human IM/MPIM history `1d`, every `p1_watch` channel, mentions today. Draft replies in chat. Never send.
3. **PRs waiting for my approve:** `gh` / GitHub search `review-requested:@me is:open`. List title, url, author, repo. This is in scope for the briefing (CODEOWNERS counts).
4. **Own PRs (P0/P2):** still list merge/CI/human review, one line each.
5. **Granola:** fold today's notes into the priority list when MCP is connected.
6. Write `<vault>/digest/YYYY-MM-DD-briefing.md` and print the same structure in chat.

## Chat / digest headings

```
# Auto-work YYYY-MM-DD HH:MM

## Tickets
## Slack
## PRs to approve
## My PRs
## Priorities
```

**Tickets:** one short paragraph per key. Status, blocker, last fact from comments or description.

**Slack:** new human messages in watch DMs/MPIMs since last tick. Draft if a reply is due.

**PRs to approve:** review-requested on me. Empty is `none`.

**My PRs:** own open PRs, only if merge-blocked by conflict/red CI or a human review comment.

**Priorities:** numbered list of what to do next, highest first. Include blocked items so they stay visible. HITL only: do not push, comment, or start a worker.

## State

Set `last_tick: briefing`. Refresh `updated`. Keep `tickets` and `p1_watch`. Do not append a live ticket to `last_ids` just because it appeared in the briefing.
