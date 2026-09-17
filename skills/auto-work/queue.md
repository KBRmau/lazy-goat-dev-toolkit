# Queue and HITL

Source: adapted from Thomas Luizon `/auto-work` for Cursor.

## Priority

1. **P0** Own PR cannot merge (conflict or required check red).
2. **P1** Slack message to you (mention or DM). Draft only. Never send.
3. **P2** Human review comment or requested changes on a PR you authored.
4. **P3** Ticket assigned to you and the ticket states what done looks like.
5. **P4** Ticket assigned, no acceptance criteria. Questions only.

One item per 15 min tick. Higher priority always wins.

Not a tick: `review-requested:@me` on someone else's PR (CODEOWNERS). Do not spend a tick reviewing other people's diffs unless the user names that PR.

`/auto-work plan` (also `draft`, `dry-run`) scans the same queue and writes a draft of what the next live tick would start. No worker, no patch. See [plan.md](plan.md).

## Acceptance criteria (P3 vs P4)

Treat as P3 only if the ticket (or linked spec) names the outcome and a way to check it. "Investigate X" or a one-line title is P4.

## P2 (your PRs)

Count only humans. Bot comments (CI, terraform plan) are not P2. Pending reviewers with no comment yet is waiting, not a tick.

## HITL

Wait for the user before:

- `git push` / creating a PR
- GitHub review comment or issue comment
- Jira transition or Jira comment
- Any Slack/Teams write (those writes are forbidden even with accept; user sends by hand)

Safe without extra accept: local branch, local commits the user did not forbid, read-only API, drafts in chat.

## Worker contract (P3)

Give the subagent: ticket key, AC verbatim, repo root, files already known, "smallest change, no extra refactors". Ask it to return: branch name, files touched, test command run, leftover risk.

## Idle

Empty inbox is a success. Do not invent chores, drive-by refactors, or extra tickets.
