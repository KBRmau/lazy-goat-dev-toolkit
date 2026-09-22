---
name: auto-work
description: >
  Work inbox loop with a fixed priority queue (P0 conflict/CI, P1 Slack,
  P2 review comments on PRs you authored, P3 ticket with spec, P4 vague
  ticket). Use when the user
  says auto-work, /auto-work, autoworker, inbox tick, standup of PRs/tickets,
  or /loop 15m /auto-work. Dry-run: /auto-work plan (also draft, dry-run).
  Builds a 07:00 weekday standup (/auto-work daily), a 15m status board
  (/auto-work briefing), a week recap (/auto-work weekly), and a monthly
  brag-doc (/auto-work brag-doc). Also handles Graphify brain queries on
  the personal cursor-brain vault. Never sends Slack/Teams.
---

# Auto-work

Personal copilot. One inbox item per tick. Public actions wait for accept.

Vault: `$CURSOR_BRAIN_VAULT` if set. Otherwise the first existing of `~/Documents/cursor-brain`, `~/OneDrive/Documentos/cursor-brain`, `~/OneDrive/Documents/cursor-brain`. State: `<vault>/state/<workspace-slug>.md`. Meetings: follow [granola.md](granola.md). Save under `<vault>/meetings/`.

Read [queue.md](queue.md) for the P0–P4 table and HITL gates.
Read [inbox.md](inbox.md) for Jira/GitHub/Slack commands.

## When invoked

1. Read this skill and `queue.md`.
2. Load or create the state file for the current workspace.
3. If the prompt is `digest` or `resumo`: follow **Daily digest**, then stop.
4. If the prompt is `daily` or `standup`: follow [daily.md](daily.md), then stop.
5. If the prompt is `briefing` or `status`: follow [briefing.md](briefing.md), then stop.
6. If the prompt is `weekly` or `semana`: follow [weekly.md](weekly.md), then stop.
7. If the prompt is `brag-doc`, `brag`, or `bragdoc`: follow [brag-doc.md](brag-doc.md), then stop.
8. If the prompt is `plan`, `draft`, or `dry-run`: follow [plan.md](plan.md), then stop.
9. If the prompt is `brain` / a question about past sessions: follow **Brain**, then stop.
10. Otherwise run **Inbox tick**.

## Inbox tick

Scan in this order. Stop at the first item that needs work. Do not start a second item in the same tick.

| Prio | Signal | Do | Wait for accept |
|------|--------|----|-----------------|
| P0 | Your PR: merge conflict or red CI | Follow `~/.cursor/skills-cursor/autopilot/SKILL.md` | push |
| P1 | Slack message to you (mention or DM). Read-only | Draft in chat. Never send. | user sends |
| P2 | Human review comment or requested changes on a PR you authored | Patch + draft reply (humanizer) | GitHub comment |
| P3 | Assigned ticket with acceptance criteria | Worker implements on a branch | open PR |
| P4 | Assigned ticket without AC | List questions. Do not code. | user scopes |

If nothing is actionable: write `idle` in state, report empty inbox, stop.

### Orchestration

- This session is the orchestrator. It does not implement P3 itself.
- P0/P2: stay here (autopilot is a loop on the current PR).
- P1: stay here. Draft only.
- P3: `Task` subagent (`generalPurpose`) with the ticket id, AC, and repo path.
- P4: `Task` `explore` only if you need repo context to ask better questions.
- After a worker returns: summarize, update state, propose the HITL action. Do not push, comment, or transition Jira until the user accepts.

### Slack

Skip P1 Slack if `user-slack` is missing or `needsAuth` (`slack.md`). When tools are listed, read unreads/mentions only. Never post, never react, never open DMs. Never OAuth from a tick. CODEOWNERS `review-requested:@me` on other people's PRs is not a tick.

### Text

Drafts (PR body, review reply, Jira comment) go through `~/.cursor/skills/humanizer/SKILL.md`. Match the user's later messages. Portuguese unless the thread is English.

### State file

```markdown
# auto-work state
workspace: <folder name>
updated: <ISO local>
last_tick: idle | plan | p0|p1|p2|p3|p4
in_flight: none | <id>
blocked: none | <reason>
last_ids: []
```

Skip an id listed in `last_ids` unless the user asks to retry. Cap `last_ids` at 30.

## Daily digest

Summarize. Do not rewrite session notes.

1. Run `python ~/.cursor/skills/auto-work/scripts/daily_digest.py`
2. Read the file it prints.
3. Optionally scan Jira assigned + GitHub review requests and append a short inbox section.
4. Do not restyle or paraphrase `sessions/*.md`. Link them.
5. Do not commit vault notes into the current project git. They stay in the vault.

## Brain

Query the personal graph, not the current repo graph:

```
graphify query "<question>" --graph "$CURSOR_BRAIN_VAULT/graphify-out/graph.json"
```

If `CURSOR_BRAIN_VAULT` is unset, resolve the vault the same way as `scripts/vault.py`. If `graph.json` is missing, say the vault has no graph yet (hook or first `graphify update` still pending).

Pasted meeting transcript: write `<vault>/meetings/YYYY-MM-DD-<slug>.md` with title, date, attendees if given, and the transcript verbatim. Then `graphify update` on the vault.

## Loop

Inbox: `/loop 15m /auto-work`. Status board: `/loop 15m /auto-work briefing`. Standup: weekday 07:00 local, prompt `/auto-work daily`. Weekly and brag-doc are on-demand (`/auto-work weekly`, `/auto-work brag-doc`). Follow `~/.cursor/skills-cursor/loop/SKILL.md`. Do not arm a loop yourself.

## Out of scope

- Sending Slack or Teams
- Simulating presence
- Slowing delivery on purpose
- Mixing two jobs in one tick (one workspace per loop)
- Committing session notes outside the vault
