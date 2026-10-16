"""Utilidades compartidas para leer las historias de docs/stories/."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
STORIES_DIR = ROOT / "docs" / "stories"
DECISIONS_FILE = ROOT / "docs" / "domain" / "decisiones-pendientes.md"

STORY_FILE_RE = re.compile(r"^(E\d{2}-\d{2})-.+\.md$")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n(.*)\Z", re.DOTALL)


@dataclass
class Story:
    path: Path
    meta: dict
    body: str
    errors: list[str] = field(default_factory=list)

    @property
    def id(self) -> str:
        return str(self.meta.get("id", ""))

    @property
    def rel(self) -> str:
        return self.path.relative_to(ROOT).as_posix()


def load_stories() -> list[Story]:
    stories: list[Story] = []
    for path in sorted(STORIES_DIR.rglob("*.md")):
        if not STORY_FILE_RE.match(path.name):
            continue
        text = path.read_text(encoding="utf-8")
        match = FRONTMATTER_RE.match(text)
        if not match:
            stories.append(
                Story(path, {}, text, ["falta el encabezado YAML entre '---'"])
            )
            continue
        try:
            meta = yaml.safe_load(match.group(1)) or {}
        except yaml.YAMLError as exc:
            stories.append(Story(path, {}, match.group(2), [f"YAML inválido: {exc}"]))
            continue
        stories.append(Story(path, meta, match.group(2)))
    return stories


def load_decision_ids() -> dict[str, str]:
    """Devuelve {D-001: estado} leyendo la tabla de decisiones-pendientes.md."""
    result: dict[str, str] = {}
    if not DECISIONS_FILE.exists():
        return result
    for line in DECISIONS_FILE.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 5 and re.fullmatch(r"D-\d{3}", cells[0]):
            result[cells[0]] = re.sub(r"[*]", "", cells[3]).strip()
    return result
