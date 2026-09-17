# Slack

Docs: https://docs.slack.dev/ai/slack-mcp-server/
Endpoint: `https://mcp.slack.com/mcp`

If Slack MCP is missing or unauthenticated: skip P1. If the user pastes a mention or thread, draft a reply in chat. Never send. Do not start OAuth from a tick.

When tools are listed and authenticated:

1. Confirm the workspace name before searching mentions.
2. Read only. Draft in chat. Never post, react, or open DMs.

If tools are missing after connect, the session still needs a restart. Stay read-only either way.
