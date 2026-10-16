#!/usr/bin/env python3
"""Valida el formato y la consistencia de docs/stories/.

Uso:
    python3 scripts/validate_stories.py                 # valida
    python3 scripts/validate_stories.py --write-index   # valida y regenera docs/stories/INDEX.md
    python3 scripts/validate_stories.py --check-index   # valida y falla si INDEX.md está desactualizado
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict

from stories_lib import ROOT, STORIES_DIR, Story, load_decision_ids, load_stories

PRIORITIES = {"must", "should", "could"}
STATUSES = {"draft", "ready", "in_progress", "done", "icebox"}
ROLES = {"admin", "technician", "owner", "dev"}
SIZES = {"XS", "S", "M", "L"}
AREAS = {"backend", "web-admin", "pwa", "infra", "datos"}
REQUIRED = [
    "id",
    "title",
    "epic",
    "phase",
    "priority",
    "status",
    "roles",
    "size",
    "areas",
    "depends_on",
    "blocked_by",
    "assumes",
]
ID_RE = re.compile(r"^E\d{2}-\d{2}$")
DEC_RE = re.compile(r"^D-\d{3}$")
LONG_DASH = (chr(0x2014), chr(0x2013))  # raya y semirraya


def validate(stories: list[Story], decisions: dict[str, str]) -> list[str]:
    errors: list[str] = []
    by_id: dict[str, Story] = {}

    def err(story: Story, msg: str) -> None:
        errors.append(f"{story.rel}: {msg}")

    for s in stories:
        for e in s.errors:
            err(s, e)
        if s.errors:
            continue
        m = s.meta
        for key in REQUIRED:
            if key not in m:
                err(s, f"falta el campo '{key}'")
        if any(k not in m for k in REQUIRED):
            continue

        sid = str(m["id"])
        if not ID_RE.match(sid):
            err(s, f"id inválido '{sid}' (formato EXX-NN)")
            continue
        if sid in by_id:
            err(s, f"id duplicado con {by_id[sid].rel}")
        by_id[sid] = s

        if not s.path.name.startswith(sid + "-"):
            err(s, "el nombre del archivo debe empezar con el id")
        if m["epic"] != sid.split("-")[0]:
            err(s, f"epic '{m['epic']}' no coincide con el id")
        if not s.path.parent.name.startswith(str(m["epic"]) + "-"):
            err(s, "el archivo debe estar en la carpeta de su épica")
        if m["phase"] not in (1, 2):
            err(s, "phase debe ser 1 o 2")
        if m["priority"] not in PRIORITIES:
            err(s, f"priority inválida '{m['priority']}'")
        if m["status"] not in STATUSES:
            err(s, f"status inválido '{m['status']}'")
        if m["size"] not in SIZES:
            err(s, f"size inválido '{m['size']}'")
        for r in m["roles"] or []:
            if r not in ROLES:
                err(s, f"rol inválido '{r}'")
        if not m["roles"]:
            err(s, "roles no puede estar vacío")
        for a in m["areas"] or []:
            if a not in AREAS:
                err(s, f"área inválida '{a}'")
        if not m["areas"]:
            err(s, "areas no puede estar vacío")
        for key in ("depends_on", "blocked_by", "assumes"):
            if not isinstance(m[key], list):
                err(s, f"{key} debe ser una lista")

        for d in (m["blocked_by"] or []) + (m["assumes"] or []):
            if not DEC_RE.match(str(d)):
                err(s, f"decisión inválida '{d}'")
            elif d not in decisions:
                err(s, f"la decisión {d} no existe en decisiones-pendientes.md")

        if m["blocked_by"] and m["status"] in {"ready", "in_progress", "done"}:
            err(
                s,
                "una historia con blocked_by no puede estar ready, in_progress ni done",
            )
        if sid.startswith("E99") and m["status"] != "icebox":
            err(s, "las historias E99 deben tener status icebox")
        if m["status"] == "icebox" and not sid.startswith("E99"):
            err(s, "status icebox solo se usa en la épica E99")

        # cuerpo
        body = s.body
        if f"# {sid} " not in body:
            err(s, f"falta el título '# {sid} ...' en el cuerpo")
        if "## Historia" not in body:
            err(s, "falta la sección '## Historia'")
        if not re.search(r"\*\*Como\*\*.+\*\*quiero\*\*.+\*\*para\*\*", body):
            err(
                s,
                "la historia debe tener el formato **Como** ..., **quiero** ..., **para** ...",
            )
        if "## Criterios de aceptación" not in body:
            err(s, "falta la sección '## Criterios de aceptación'")
        elif not re.search(r"^1\. ", body, re.MULTILINE):
            err(s, "los criterios de aceptación deben ser una lista numerada")
        text = s.path.read_text(encoding="utf-8")
        if any(c in text for c in LONG_DASH):
            err(s, "contiene guion largo (usar guion simple '-')")

    # referencias entre historias
    for sid, s in by_id.items():
        for dep in s.meta["depends_on"] or []:
            if dep not in by_id:
                errors.append(
                    f"{s.rel}: depends_on referencia una historia inexistente '{dep}'"
                )
            elif dep == sid:
                errors.append(f"{s.rel}: depende de sí misma")
            elif (
                s.meta["status"] in {"ready", "in_progress", "done"}
                and by_id[dep].meta["status"] == "icebox"
            ):
                errors.append(f"{s.rel}: depende de {dep}, que está en icebox")
        for ref in set(re.findall(r"\bE\d{2}-\d{2}\b", s.body)):
            if ref not in by_id:
                errors.append(f"{s.rel}: menciona una historia inexistente '{ref}'")

    # ciclos
    graph = {
        sid: [d for d in (s.meta["depends_on"] or []) if d in by_id]
        for sid, s in by_id.items()
    }
    state: dict[str, int] = {}

    def visit(node: str, path: list[str]) -> None:
        if state.get(node) == 2:
            return
        if state.get(node) == 1:
            cycle = " -> ".join(path[path.index(node) :] + [node])
            errors.append(f"ciclo de dependencias: {cycle}")
            return
        state[node] = 1
        for nxt in graph[node]:
            visit(nxt, path + [node])
        state[node] = 2

    for node in graph:
        visit(node, [])

    # referencias a historias desde otros documentos
    for doc in list((ROOT / "docs").rglob("*.md")) + [
        ROOT / "CLAUDE.md",
        ROOT / "README.md",
    ]:
        if STORIES_DIR in doc.parents:
            continue
        for ref in set(
            re.findall(r"\bE\d{2}-\d{2}\b", doc.read_text(encoding="utf-8"))
        ):
            if ref not in by_id and ref not in {"E00-00", "EXX-NN"}:
                errors.append(
                    f"{doc.relative_to(ROOT).as_posix()}: menciona una historia inexistente '{ref}'"
                )

    return errors


def build_index(stories: list[Story], decisions: dict[str, str]) -> str:
    epics: dict[str, list[Story]] = defaultdict(list)
    for s in stories:
        epics[s.meta["epic"]].append(s)

    total = len(stories)
    by_status: dict[str, int] = defaultdict(int)
    for s in stories:
        by_status[s.meta["status"]] += 1

    prio = {"must": "Debe", "should": "Debería", "could": "Podría"}
    lines = [
        "# Índice de historias",
        "",
        "> Generado por `python3 scripts/validate_stories.py --write-index`. No editar a mano.",
        "",
        f"**Total: {total} historias.** "
        + ", ".join(f"{k}: {v}" for k, v in sorted(by_status.items())),
        "",
        "Leyenda: **Bloq.** = decisión abierta que impide implementarla. **Supone** = decisión con propuesta vigente en la que se apoya.",
        "",
    ]
    for epic in sorted(epics):
        folder = epics[epic][0].path.parent.name
        readme = (
            (STORIES_DIR / folder / "README.md")
            .read_text(encoding="utf-8")
            .splitlines()[0]
        )
        lines += [
            f"## {readme.lstrip('# ').strip()}",
            "",
            "| ID | Historia | Prioridad | Tamaño | Estado | Roles | Bloq. | Supone | Depende de |",
            "|---|---|---|---|---|---|---|---|---|",
        ]
        for s in sorted(epics[epic], key=lambda x: x.id):
            m = s.meta
            rel = s.path.relative_to(STORIES_DIR).as_posix()
            lines.append(
                f"| [{m['id']}]({rel}) | {m['title']} | {prio[m['priority']]} | {m['size']} | {m['status']} "
                f"| {', '.join(m['roles'])} | {', '.join(m['blocked_by']) or '-'} "
                f"| {', '.join(m['assumes']) or '-'} | {', '.join(m['depends_on']) or '-'} |"
            )
        lines.append("")

    blocked: dict[str, list[str]] = defaultdict(list)
    for s in stories:
        for d in s.meta["blocked_by"]:
            blocked[d].append(s.id)
    lines += [
        "## Historias bloqueadas por decisión",
        "",
        "| Decisión | Estado | Historias bloqueadas |",
        "|---|---|---|",
    ]
    for d in sorted(blocked):
        lines.append(
            f"| {d} | {decisions.get(d, '?')} | {', '.join(sorted(blocked[d]))} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write-index", action="store_true")
    ap.add_argument("--check-index", action="store_true")
    args = ap.parse_args()

    stories = load_stories()
    decisions = load_decision_ids()
    errors = validate(stories, decisions)
    if errors:
        print(f"{len(errors)} problema(s) en las historias:\n")
        for e in errors:
            print(" -", e)
        return 1

    index = build_index(stories, decisions)
    index_path = STORIES_DIR / "INDEX.md"
    if args.write_index:
        index_path.write_text(index, encoding="utf-8")
        print(f"INDEX.md actualizado ({len(stories)} historias)")
    elif args.check_index:
        current = index_path.read_text(encoding="utf-8") if index_path.exists() else ""
        if current != index:
            print(
                "docs/stories/INDEX.md está desactualizado. Correr: python3 scripts/validate_stories.py --write-index"
            )
            return 1
    print(f"OK: {len(stories)} historias válidas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
