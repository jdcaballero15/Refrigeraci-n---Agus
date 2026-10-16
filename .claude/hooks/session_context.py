#!/usr/bin/env python3
"""Hook SessionStart: informa al agente el estado real del repositorio.

Un agente que arranca en frio no sabe en que rama esta ni que historias estan en curso.
Sin esto, lo primero que intenta puede ser bloqueado por otro hook.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


def git(*args: str) -> str | None:
    try:
        out = subprocess.run(["git", *args], capture_output=True, text=True, timeout=5, check=False)
    except (OSError, subprocess.SubprocessError):
        return None
    return out.stdout.strip() if out.returncode == 0 else None


def story_counts(root: Path) -> dict[str, int]:
    counts: dict[str, int] = {}
    for md in (root / "docs" / "stories").glob("E*/E*.md"):
        head = md.read_text(encoding="utf-8").split("---", 2)
        match = re.search(r"^status:\s*(\w+)", head[1], re.MULTILINE) if len(head) > 2 else None
        if match:
            counts[match.group(1)] = counts.get(match.group(1), 0) + 1
    return counts


def main() -> None:
    raw_root = git("rev-parse", "--show-toplevel")
    if raw_root is None:
        return
    root = Path(raw_root)
    branch = git("rev-parse", "--abbrev-ref", "HEAD") or "desconocida"
    dirty = git("status", "--porcelain") or ""

    lines = [
        "Estado del repositorio OT Platform al iniciar la sesion:",
        f"- Rama actual: {branch}",
        f"- Cambios sin commitear: {len(dirty.splitlines())} archivo(s)",
    ]
    if branch == "main":
        lines.append(
            "- ATENCION: 'main' esta protegida. Los hooks bloquean escrituras y commits "
            "hasta crear una rama (feat/EXX-NN-descripcion). Ver CONTRIBUTING.md."
        )
    counts = story_counts(root)
    if counts:
        resumen = ", ".join(f"{k}: {v}" for k, v in sorted(counts.items()))
        lines.append(f"- Historias por estado: {resumen}")
        lines.append("- Solo se implementan historias en 'ready' y sin 'blocked_by'.")
    print("\n".join(lines))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001
        print(f"[session_context] {exc}", file=sys.stderr)
    sys.exit(0)
