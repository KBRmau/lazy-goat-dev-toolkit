#!/usr/bin/env python3
"""Build today's digest from session notes. Does not rewrite note bodies."""
from __future__ import annotations

import sys
from datetime import datetime, timedelta
from pathlib import Path

from vault import resolve_vault

VAULT = resolve_vault()
SESSIONS = VAULT / "sessions"
MEETINGS = VAULT / "meetings"
DIGEST = VAULT / "digest"


def first_heading(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "(sem titulo)"


def list_recent(folder: Path, since: datetime) -> list[Path]:
    if not folder.is_dir():
        return []
    out = []
    for p in folder.glob("*.md"):
        if p.stat().st_mtime >= since.timestamp():
            out.append(p)
    out.sort(key=lambda x: x.stat().st_mtime)
    return out


def main() -> int:
    DIGEST.mkdir(parents=True, exist_ok=True)
    now = datetime.now()
    since = now - timedelta(hours=24)
    day = now.strftime("%Y-%m-%d")
    dest = DIGEST / f"{day}.md"
    sessions = list_recent(SESSIONS, since)
    meetings = list_recent(MEETINGS, since)
    lines = [
        f"# Digest {day}",
        "",
        f"Janela: {since.strftime('%Y-%m-%d %H:%M')} -> {now.strftime('%Y-%m-%d %H:%M')}.",
        "Indice das notas. Corpos em `sessions/` e `meetings/` nao foram reescritos.",
        "",
        f"## Sessoes ({len(sessions)})",
        "",
    ]
    if not sessions:
        lines.append("Nenhuma sessao nas ultimas 24h.")
        lines.append("")
    for p in sessions:
        title = first_heading(p.read_text(encoding="utf-8", errors="replace"))
        rel = p.relative_to(VAULT).as_posix()
        lines.append(f"- [{title}]({rel})")
    lines.extend(["", f"## Reunioes coladas ({len(meetings)})", ""])
    if not meetings:
        lines.append("Nenhum transcript colado nas ultimas 24h.")
        lines.append("")
    for p in meetings:
        title = first_heading(p.read_text(encoding="utf-8", errors="replace"))
        rel = p.relative_to(VAULT).as_posix()
        lines.append(f"- [{title}]({rel})")
    lines.extend(
        [
            "",
            "## Inbox",
            "",
            "Preencher no tick `/auto-work digest` (Jira assigned + review requests).",
            "Nao inventar itens aqui.",
            "",
        ]
    )
    dest.write_text("\n".join(lines), encoding="utf-8")
    print(dest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
