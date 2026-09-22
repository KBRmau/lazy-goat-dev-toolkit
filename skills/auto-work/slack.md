# Slack

Local stdio MCP: [`korotovsky/slack-mcp-server`](https://github.com/korotovsky/slack-mcp-server) (`npx -y slack-mcp-server@latest --transport stdio`). Tokens stay in local `mcp.json` env. Not in this git.

Enabled tools (read-only): `conversations_history`, `conversations_replies`, `conversations_search_messages`, `conversations_unreads`, `channels_list`, `channels_me`, `users_search`, `usergroups_list`.

Do not enable write tools (`conversations_add_message`, `reactions_add`, `reactions_remove`). Never post, react, or open DMs from a tick.

## P1 tick

If namespace `user-slack` is missing or `needsAuth`: skip P1, one sentence in the report. Do not start OAuth from a tick. If the user pastes a thread, draft in chat.

When tools are listed:

1. `conversations_unreads` with `mentions_only: true` (and DMs via `channel_types: dm` if needed).
2. Optional: `conversations_search_messages` for today's mentions (`filter_date_on: Today`).
3. Draft the reply in chat. User sends by hand.

Stay read-only even if a write tool appears later.
