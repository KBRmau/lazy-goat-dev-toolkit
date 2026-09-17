from __future__ import annotations

import os
from pathlib import Path

ENV = "CURSOR_BRAIN_VAULT"


def resolve_vault() -> Path:
    """Vault dir: $CURSOR_BRAIN_VAULT, else the first existing default, else ~/Documents/cursor-brain."""
    raw = os.environ.get(ENV, "").strip()
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
