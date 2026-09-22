# Catálogo

O que o Lazy Goat Dev Toolkit documenta. Listas de nomes: `agency-skills.txt`, `agents-skills.txt`, `cursor-builtin-skills.txt`.

## Skills deste repo (`~/.cursor/skills` depois do install)

| Skill | Quando |
| --- | --- |
| `auto-work` | Inbox, digest, standup, briefing, weekly, brag-doc, brain |
| `humanizer` | Prosa visível. Regra: `rules/humanizer.mdc`. Upstream: https://github.com/blader/humanizer |

## Regras always-on (`~/.cursor/rules`)

| Arquivo | Função |
| --- | --- |
| `humanizer.mdc` | Prosa |
| `graphify.mdc` | Query `graphify-out/` do repo atual. Upstream: https://github.com/Graphify-Labs/graphify |

As regras `agency-*.mdc` vêm do pacote agency. São requestable. Não estão neste git.

## Agency agents

Pacote: https://github.com/msitarzewski/agency-agents

Instala em `~/.cursor/skills/agency-*`. Nomes em [agency-skills.txt](agency-skills.txt).

Se o pedido for desenvolver ou revisar sem nomear um agente, ler `agency-agents-orchestrator` e carregar só os skills do domínio.

No código: `agency-agents-orchestrator`, `agency-minimal-change-engineer`, `agency-technical-writer`, `agency-git-workflow-master`, `agency-code-reviewer`, `agency-frontend-developer`, `agency-backend-architect`, `agency-database-optimizer`.

## `~/.agents/skills`

Não copiados. Instalação de terceiros.

Índice: https://skills.sh/

| Skill | Função | Fonte |
| --- | --- | --- |
| `graphify` | Grafo do repo (`query` / `path` / `explain` / `update`). CLI: `uv tool install graphifyy`. | https://github.com/Graphify-Labs/graphify |
| `find-skills` | `npx skills find` | https://skills.sh/ |
| `orchestration` | Mensagens Orca, DAG, `worker_done` | Orca |
| `orca-cli` | Worktrees, terminais e browser do Orca | Orca |
| `computer-use` | UI desktop via `orca computer` | Orca |

## Built-in Cursor (`~/.cursor/skills-cursor`)

O Cursor atualiza essa pasta. auto-work chama `autopilot` (P0) e `loop` (inbox 15 min / standup).

Também úteis: `create-skill`, `create-rule`, `new-repo`, `canvas`, `review`, `review-bugbot`, `review-security`.

Lista: [cursor-builtin-skills.txt](cursor-builtin-skills.txt).

## MCP

Tokens em `~/.cursor/mcp.json` local. Fora deste git.

| Namespace | Uso | Docs / endpoint |
| --- | --- | --- |
| Atlassian | Jira P3/P4. Transições depois do accept. | https://github.com/atlassian/atlassian-mcp-server e `https://mcp.atlassian.com/v2/mcp` |
| GitHub | PRs seus, reviews. | https://github.com/github/github-mcp-server e `https://api.githubcopilot.com/mcp/` |
| Slack | P1 (mentions/DMs). Nunca postar. Stdio `npx slack-mcp-server`. | https://github.com/korotovsky/slack-mcp-server |
| Trello | Quadros. | https://github.com/atlassian/trello-mcp-server e `https://mcp.trello.com/v1` |
| Magnific | Imagem e vídeo. | https://www.magnific.com/mcp , https://docs.magnific.com/modelcontextprotocol e `https://mcp.magnific.com` |
| Meta Ads | Ads. | https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-overview e `https://mcp.facebook.com/ads` |
| Figma | Design. | https://github.com/figma/mcp-server-guide e `https://mcp.figma.com/mcp` |
| Stripe | Conta Stripe. Plugin ou `https://mcp.stripe.com`. | https://docs.stripe.com/mcp e https://github.com/stripe/ai |
| Granola | Reuniões. OAuth remoto. | `https://mcp.granola.ai/mcp` |

## Vault

Pasta local `cursor-brain` (sessions, digest, state, meetings, grafo pessoal). Path: `$CURSOR_BRAIN_VAULT` ou os defaults em `skills/auto-work/scripts/vault.py`. Não commitar o vault no git do projeto em que você está.

O hook `sessionEnd` grava uma nota curta em `<vault>/sessions/`. O Graphify pode indexar.
