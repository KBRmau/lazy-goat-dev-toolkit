# Plan / draft (no work)

Dry-run of one inbox tick. Read-only.

## Trigger

`/auto-work plan` or `draft` or `dry-run`. Cursor Plan mode is unrelated.

## Do

1. Scan the same sources as an inbox tick (`inbox.md`): own PRs (P0), Slack unreads/mentions if `user-slack` is listed (P1), human reviews on PRs you authored (P2), assigned Jira (P3/P4). Granola is standup/digest, not a queue tick. Do not treat `review-requested:@me` on other people's PRs as a tick.
2. Walk P0 then P1 then P2 then P3 then P4. Mark the first item that a live tick would start. Mark later items as waiting.
3. Honour `last_ids` in the state file: label those skip (already seen) unless the user said retry.
4. Write `<vault>/digest/YYYY-MM-DD-plan.md` and summarise in chat.

## Headings

```
# Auto-work plan YYYY-MM-DD HH:MM

## Next tick
## Waiting
## Skipped (last_ids)
## Would not do
```

**Next tick:** one item. Priority, id, URL, what the live tick would do, what still needs accept.

**Waiting:** the rest, one line each, why they lose (lower prio or blocked).

**Would not do:** no worker, no patch, no push, no GitHub/Jira write, no Slack send, no `last_ids` append.

## Stop

Do not start autopilot. Do not spawn a P3 worker. Do not edit repo files. Do not change `in_flight`. You may refresh `updated` on the state file with `last_tick: plan`.
