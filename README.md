# Lazy Goat Dev Toolkit

<p align="center">
  <img src="docs/lazy-goat.png" alt="Cabra preguiçosa no escritório, ao lado de um laptop" width="720">
</p>

Skills e regras para o Cursor: auto-work (inbox), humanizer, Graphify. Catálogo do Graphify, agency-agents e das MCPs que o toolkit usa.

Notas do vault ficam fora do git, numa pasta local `cursor-brain`. `mcp.json` fica na máquina.

## Links

- Graphify: https://github.com/Graphify-Labs/graphify
- Agency agents: https://github.com/msitarzewski/agency-agents
- Skills CLI: https://skills.sh/
- Tabela de MCP: [catalog/CATALOG.md](catalog/CATALOG.md)

## Layout

| Path | Conteúdo |
| --- | --- |
| `skills/auto-work/` | Inbox P0–P4, digest, standup, briefing, weekly, brag-doc, brain |
| `skills/humanizer/` | Prosa 3.0.0 |
| `rules/` | `humanizer.mdc`, `graphify.mdc` (`alwaysApply`) |
| `hooks/session_end_graphify.py` | Nota de fim de sessão no vault |
| `catalog/` | Nomes do pacote e URLs das MCPs |

## Path do vault

Defina `CURSOR_BRAIN_VAULT` se quiser um diretório fixo. Copie [.env.example](.env.example).

Se a variável estiver vazia, o Python usa a primeira pasta que existir:

- `~/Documents/cursor-brain`
- `~/OneDrive/Documentos/cursor-brain`
- `~/OneDrive/Documents/cursor-brain`

Senão usa `~/Documents/cursor-brain`.

## Auto-work

Um item de inbox por tick. Não envia Slack.

| Comando | Efeito |
| --- | --- |
| `/auto-work` | Tick da fila |
| `/auto-work digest` ou `resumo` | Índice 24h em `<vault>/digest/` |
| `/auto-work daily` | Standup |
| `/auto-work briefing` | Quadro de status (loop 15 min) |
| `/auto-work weekly` ou `semana` | Recap da semana ISO (`<vault>/digest/YYYY-Www-weekly.md`) |
| `/auto-work brag-doc` | Brag-doc mensal (`<vault>/brag.md`) |
| `/auto-work plan` | Dry-run (também `draft`, `dry-run`) |
| `/auto-work brain` | Query Graphify no vault |
| `/loop 15m /auto-work` | Loop de inbox |

Fila: P0 CI/conflito no PR seu, P1 Slack (MCP stdio, só leitura), P2 review humano no PR seu, P3 ticket com critério, P4 ticket vago.

## Instalar

```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

Copie o bloco `sessionEnd` de `hooks/sessionEnd.example.json` para `~/.cursor/hooks.json`. No Windows, troque `~` por `%USERPROFILE%` nesse comando. Não apague outros hooks.

## Catálogo

[catalog/CATALOG.md](catalog/CATALOG.md)
