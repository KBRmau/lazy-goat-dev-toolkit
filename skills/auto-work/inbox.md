# Inbox recipes

Use tools that exist in the current session. Skip a source that is missing.

## GitHub

Prefer `user-github` MCP when listed. Fallback: `gh`.

```
gh pr list --author @me --state open
gh pr status
gh search issues --assignee=@me --state=open
```

P0: for each open PR you authored, `gh pr view <n> --json mergeable,mergeStateStatus,statusCheckRollup,url,title`.
P2: on those same PRs, `get_reviews` + `get_review_comments` + human issue comments. Ignore bot comments (CI, terraform plan). Do not query `review-requested:@me` as a tick source.

Do not `gh pr comment` or `gh pr create` until accept.

## Jira

Prefer Atlassian MCP (`jira_search`, `jira_get_issue`, `jira_get_transitions`).

Search assigned to current user, status not Done, order by updated. Read description + comments before classifying P3 vs P4.

Do not `jira_transition_issue` or `jira_add_comment` until accept.

## Slack

See [slack.md](slack.md). Namespace `user-slack` (`slack-mcp-server` stdio).

If tools are listed: `conversations_unreads` (mentions/DMs) and optional `conversations_search_messages`. Draft in chat. Never post.

If the namespace is `needsAuth` or absent: skip P1 Slack, one sentence in the tick report. Do not start OAuth from a tick.

## Meetings

See [granola.md](granola.md). Namespace `user-granola`.

If tools are listed: `list_meetings` or `query_granola_meetings` for notes you own, then save markdown under `<vault>/meetings/`. If absent, the user pastes the transcript (or CSV export). Index with Graphify. Do not scrape the Granola app folder.
