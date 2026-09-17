# Granola

Endpoint: `https://mcp.granola.ai/mcp` (OAuth). Do not put tokens in `mcp.json`.

Until MCP tools are listed: user pastes the transcript. Save under `<vault>/meetings/YYYY-MM-DD-<slug>.md` and run `graphify update` on the vault.

When connected:

1. Call `get_account_info` (or equivalent) and confirm the signed-in account.
2. Pull notes/transcripts you own.
3. Write each meeting to `<vault>/meetings/` (verbatim transcript + title/date). Then Graphify update. Do not rewrite the transcript.

Free/Basic MCP: last 30 days; `get_meeting_transcript` is paid-plan. If transcript tools are missing, ask the user to paste or use Settings > Profile > Generate CSV.

Never scrape the Granola desktop folder. Prefer official MCP, then paste, then CSV export.
