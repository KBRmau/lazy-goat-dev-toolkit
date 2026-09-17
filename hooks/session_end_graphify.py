#!/usr/bin/env python3
"""Cursor sessionEnd hook: write a short note into the personal Graphify vault.

Fail open. Never block session close. Does not dump full tool payloads or secrets.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import traceback
from datetime import datetime
from pathlib import Path

def resolve_vault() -> Path:
    raw = os.environ.get("CURSOR_BRAIN_VAULT", "").strip()
    if raw:
        return Path(raw).expanduser().resolve()
    home = Path.home()
    candidates = [
        home / "Documents" / "cursor-brain",
        home / "OneDrive" / "Documentos" / "cursor-brain",
        home / "OneDrive" / "Documents" / "cursor-brain",
    ]
    for path in candidates:
        if path.is_dir():
            return path.resolve()
    return candidates[0]


VAULT = resolve_vault()
SESSIONS = VAULT / "sessions"
PROJECTS = Path.home() / ".cursor" / "projects"
MAX_CHARS = 4000
SECRET_RE = re.compile(
    r"(?i)(api[_-]?key|token|secret|password|passwd|bearer)\s*[:=]\s*\S+"
    r"|ghp_[A-Za-z0-9]+"
    r"|gho_[A-Za-z0-9]+"
    r"|ATATT[A-Za-z0-9_\-=]+"
    r"|sk-[A-Za-z0-9]+"
)


def redact(text: str) -> str:
    return SECRET_RE.sub("[redacted]", text or "")


def slug(text: str, n: int = 48) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", (text or "").strip().lower()).strip("-")
    return (s[:n] or "session").rstrip("-")


def read_stdin() -> dict:
    raw = sys.stdin.read()
    if not raw.strip():
        return {}
    try:
        data = json.loads(raw)
        return data if isinstance(data, dict) else {"_raw": data}
    except json.JSONDecodeError:
        return {"_unparsed": raw[:2000]}


def pick(d: dict, *keys: str) -> str:
    for k in keys:
        v = d.get(k)
        if v:
            return str(v)
    return ""


def extract_text_blocks(obj) -> list[str]:
    out: list[str] = []
    if isinstance(obj, dict):
        role = obj.get("role")
        msg = obj.get("message") or obj.get("content")
        if role in ("user", "assistant") and msg is not None:
            chunks = []
            if isinstance(msg, dict):
                content = msg.get("content", [])
                if isinstance(content, str):
                    chunks.append(content)
                elif isinstance(content, list):
                    for part in content:
                        if isinstance(part, dict) and part.get("type") == "text":
                            chunks.append(part.get("text") or "")
                        elif isinstance(part, str):
                            chunks.append(part)
            elif isinstance(msg, str):
                chunks.append(msg)
            text = "\n".join(c for c in chunks if c).strip()
            text = re.sub(r"</?user_query>", "", text)
            text = re.sub(r"<timestamp>.*?</timestamp>", "", text, flags=re.S)
            if text:
                out.append(f"## {role}\n\n{text[:1200]}")
        else:
            for v in obj.values():
                out.extend(extract_text_blocks(v))
    elif isinstance(obj, list):
        for item in obj:
            out.extend(extract_text_blocks(item))
    return out


def find_transcript(payload: dict) -> Path | None:
    direct = pick(payload, "transcript_path", "transcriptPath", "transcript")
    if direct:
        p = Path(direct)
        if p.is_file():
            return p
    conv = pick(
        payload,
        "conversation_id",
        "conversationId",
        "session_id",
        "sessionId",
        "generation_id",
        "generationId",
    )
    if not conv or not PROJECTS.is_dir():
        return None
    matches = list(PROJECTS.glob(f"**/agent-transcripts/**/{conv}.jsonl"))
    if not matches:
        matches = list(PROJECTS.glob(f"**/*{conv}*.jsonl"))
    if not matches:
        return None
    matches.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return matches[0]


def transcript_excerpt(path: Path) -> tuple[str, str]:
    user_first = ""
    blocks: list[str] = []
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return "", ""
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        extracted = extract_text_blocks(obj)
        if not user_first:
            for b in extracted:
                if b.startswith("## user"):
                    user_first = b.split("\n", 2)[-1].strip()
                    break
        blocks.extend(extracted)
    body = "\n\n".join(blocks[:12])
    if len(body) > MAX_CHARS:
        body = body[:MAX_CHARS] + "\n\n[truncated]"
    return user_first, redact(body)


def workspace_name(payload: dict) -> str:
    roots = payload.get("workspace_roots") or payload.get("workspaceRoots") or []
    if isinstance(roots, list) and roots:
        return Path(str(roots[0])).name
    cwd = pick(payload, "cwd", "workspace", "root")
    if cwd:
        return Path(cwd).name
    return "unknown"


def spawn_graphify_update() -> None:
    stamp = VAULT / "graphify-out" / ".last-update"
    stamp.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now().timestamp()
    if stamp.exists() and (now - stamp.stat().st_mtime) < 120:
        return
    stamp.write_text(str(now), encoding="utf-8")
    graphify = shutil_which("graphify")
    if not graphify:
        return
    flags = 0
    if os.name == "nt":
        flags = subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
    subprocess.Popen(
        [graphify, "update", str(VAULT), "--no-cluster"],
        cwd=str(VAULT),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=flags,
    )


def shutil_which(cmd: str) -> str | None:
    from shutil import which

    return which(cmd)


def main() -> int:
    payload = read_stdin()
    SESSIONS.mkdir(parents=True, exist_ok=True)
    now = datetime.now()
    ws = workspace_name(payload)
    conv = pick(
        payload,
        "conversation_id",
        "conversationId",
        "session_id",
        "sessionId",
    )
    tpath = find_transcript(payload)
    title, excerpt = ("", "")
    if tpath:
        title, excerpt = transcript_excerpt(tpath)
    title = title.split("\n", 1)[0][:80] or "session"
    fname = f"{now.strftime('%Y-%m-%d-%H%M%S')}-{slug(ws)}-{slug(title, 32)}.md"
    dest = SESSIONS / fname
    meta_keys = sorted(k for k in payload.keys() if not str(k).startswith("_"))
    lines = [
        "---",
        f"date: {now.isoformat(timespec='seconds')}",
        f"workspace: {ws}",
        f"conversation: {conv}",
        f"source: cursor-sessionEnd",
        "---",
        "",
        f"# {title}",
        "",
        f"- workspace: `{ws}`",
        f"- conversation: `{conv or 'unknown'}`",
        f"- payload keys: {', '.join(meta_keys) or '(empty)'}",
        "",
    ]
    if tpath:
        lines.append(f"- transcript: `{tpath}`")
        lines.append("")
    lines.append(excerpt or "_No transcript text found in the hook payload._")
    lines.append("")
    dest.write_text("\n".join(lines), encoding="utf-8")
    try:
        spawn_graphify_update()
    except Exception:
        traceback.print_exc(file=sys.stderr)
    # sessionEnd has no required stdout schema; empty success.
    sys.stdout.write("{}\n")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception:
        traceback.print_exc(file=sys.stderr)
        sys.stdout.write("{}\n")
        raise SystemExit(0)
