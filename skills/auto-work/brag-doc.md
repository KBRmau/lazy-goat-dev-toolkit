# Brag-doc

High points of work done so far, grouped by calendar month. Portuguese. Humanizer. Promotion/1:1 material. Facts only. Do not inflate. Do not list every ticket.

## Trigger

`/auto-work brag-doc`, `brag`, or `bragdoc`. On-demand. Do not treat this as an inbox tick.

## Scope

Assigned Jira that reached Done/Closed/Resolved (or the local equivalent) and PRs you authored that merged. Skip personal forks unless the user asks to include them. Skip Won't Do. Skip open tickets unless a concrete high already landed (comment, measurement, merge) and you label it as in progress.

If the user names a GitHub org, add `--owner <org>` to the PR search. Do not assume an org.

## Sources (skip missing)

1. Existing `<vault>/brag.md` (keep months that still have evidence; add new highs; drop a bullet only if it was wrong).
2. Jira: `assignee = currentUser() AND status in (Done, Closed, Resolved) ORDER BY resolutiondate DESC` (paginate, cap 50). Read summary + resolution date. Do not use Updated as the month if resolutiondate exists.
3. GitHub: `gh search prs --author=@me --merged --limit 50`. Group by `closedAt` month (UTC).
4. Vault digest/standup/weekly for in-progress highs that are not yet Done. Cite the ticket.
5. Granola/meetings only if they record a decision you owned.

Do not invent impact ("saved X", "unblocked the org") unless a source states it.

## Output (chat + vault)

Overwrite `<vault>/brag.md` with:

```
# Brag-doc

Atualizado: YYYY-MM-DD

## YYYY-MM
```

Newest month first. Under each month, 3 to 8 bullets max. Each bullet: outcome + ticket/PR. Prefer merged/Done items. One in-progress bullet is allowed if it is already a high (shipped a POC, posted a measured finding).

Optional snapshot copy: `<vault>/digest/YYYY-MM-DD-brag.md` (same body). Use this when the user asks to keep history of previous runs.

Do not commit these files into the current project git. They stay in the vault.
