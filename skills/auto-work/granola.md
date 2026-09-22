# Granola

Official remote MCP: `https://mcp.granola.ai/mcp` (OAuth). Do not put tokens in `mcp.json`.

Cursor namespace: `user-granola`. Tools: `get_account_info`, `query_granola_meetings`, `list_meetings`, `get_meetings`, `get_meeting_transcript`, `list_meeting_folders`.

If the namespace is missing or `needsAuth`: user pastes the transcript. Save under `<vault>/meetings/YYYY-MM-DD-<slug>.md` and run `graphify update` on the vault.

When connected:

1. `get_account_info` if you need to confirm the signed-in account.
2. For standup / digest (last 24h): `list_meetings` (narrow with `involvement.captured_by_me` when the user asked for their notes) or `query_granola_meetings`.
3. For a specific meeting: `get_meetings` then `get_meeting_transcript` when the user needs verbatim quotes.
4. Write each meeting you persist to `<vault>/meetings/` (title, date, attendees if given, transcript or notes). Then Graphify update. Do not rewrite the transcript.

Never scrape the Granola desktop folder. Prefer MCP, then paste, then CSV export.
