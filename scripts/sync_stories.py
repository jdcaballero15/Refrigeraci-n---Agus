#!/usr/bin/env python3
"""Crea o actualiza un issue de GitHub por cada historia de docs/stories/.

- Identifica el issue por el ID en el título: "[E04-03] Asignar una orden a un técnico".
- Nunca cierra ni borra issues.
- Solo administra las etiquetas con prefijos epica:, prioridad:, estado:, fase:, area:, y la etiqueta bloqueada.
- Requiere `gh` autenticado (en Actions, con GH_TOKEN) salvo en --dry-run.

Uso:
    python3 scripts/sync_stories.py --dry-run     # muestra qué haría, sin llamar a GitHub
    python3 scripts/sync_stories.py               # sincroniza
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time

from stories_lib import Story, load_stories

MARKER = "<!-- story-sync:{id} -->"
PRIORITY = {"must": "debe", "should": "deberia", "could": "podria"}
STATE = {
    "draft": "borrador",
    "ready": "lista",
    "in_progress": "en-curso",
    "done": "hecha",
    "icebox": "icebox",
}
MANAGED_PREFIXES = ("epica:", "prioridad:", "estado:", "fase:", "area:")
MANAGED_EXACT = {"bloqueada", "tipo:historia"}


def desired_labels(s: Story) -> set[str]:
    m = s.meta
    labels = {
        "tipo:historia",
        f"epica:{s.path.parent.name}",
        f"prioridad:{PRIORITY[m['priority']]}",
        f"estado:{STATE[m['status']]}",
        f"fase:{m['phase']}",
    }
    labels |= {f"area:{a}" for a in m["areas"]}
    if m["blocked_by"]:
        labels.add("bloqueada")
    return labels


def issue_body(s: Story, repo: str) -> str:
    m = s.meta
    link = f"https://github.com/{repo}/blob/main/{s.rel}"
    # El cuerpo de la historia sin el título H1 (el título ya es el del issue)
    body = re.sub(r"\A\s*# .*\n", "", s.body, count=1).strip()
    head = [
        MARKER.format(id=s.id),
        f"> Este issue se genera desde [`{s.rel}`]({link}). **Editar el archivo, no el issue.**",
        "",
        "| Campo | Valor |",
        "|---|---|",
        f"| Épica | {m['epic']} |",
        f"| Prioridad | {m['priority']} |",
        f"| Tamaño | {m['size']} |",
        f"| Estado | {m['status']} |",
        f"| Roles | {', '.join(m['roles'])} |",
        f"| Depende de | {', '.join(m['depends_on']) or '-'} |",
        f"| Bloqueada por | {', '.join(m['blocked_by']) or '-'} |",
        f"| Supone | {', '.join(m['assumes']) or '-'} |",
        "",
        "",
    ]
    return "\n".join(head) + body + "\n"


def gh(*args: str, input_text: str | None = None) -> str:
    result = subprocess.run(
        ["gh", *args], capture_output=True, text=True, input=input_text, check=False
    )
    if result.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args[:3])} falló: {result.stderr.strip()}")
    return result.stdout


def existing_issues() -> dict[str, dict]:
    out = gh(
        "issue",
        "list",
        "--label",
        "tipo:historia",
        "--state",
        "all",
        "--limit",
        "1000",
        "--json",
        "number,title,body,labels",
    )
    found: dict[str, dict] = {}
    for issue in json.loads(out):
        m = re.match(r"^\[(E\d{2}-\d{2})\]", issue["title"])
        if m:
            found[m.group(1)] = issue
    return found


def repo_name() -> str:
    env = os.environ.get("GITHUB_REPOSITORY")
    if env:
        return env
    return json.loads(gh("repo", "view", "--json", "nameWithOwner"))["nameWithOwner"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    stories = load_stories()
    if args.dry_run:
        repo = os.environ.get("GITHUB_REPOSITORY", "jdcaballero15/Refrigeraci-n---Agus")
        for s in stories:
            title = f"[{s.id}] {s.meta['title']}"
            print(
                f"CREAR/ACTUALIZAR  {title}\n    etiquetas: {', '.join(sorted(desired_labels(s)))}"
            )
        print(
            f"\n{len(stories)} historias (dry-run, no se llamó a GitHub). Repo: {repo}"
        )
        return 0

    repo = repo_name()
    issues = existing_issues()
    created = updated = unchanged = 0
    for s in stories:
        title = f"[{s.id}] {s.meta['title']}"
        body = issue_body(s, repo)
        labels = desired_labels(s)
        current = issues.get(s.id)
        if current is None:
            cmd = ["issue", "create", "--title", title, "--body-file", "-"]
            for lb in sorted(labels):
                cmd += ["--label", lb]
            gh(*cmd, input_text=body)
            created += 1
            time.sleep(1.5)  # evita límites secundarios de la API
            continue

        current_labels = {lb["name"] for lb in current["labels"]}
        managed = {
            lb
            for lb in current_labels
            if lb.startswith(MANAGED_PREFIXES) or lb in MANAGED_EXACT
        }
        add = sorted(labels - current_labels)
        remove = sorted(managed - labels)
        if (
            current["title"] == title
            and current["body"].strip() == body.strip()
            and not add
            and not remove
        ):
            unchanged += 1
            continue
        cmd = [
            "issue",
            "edit",
            str(current["number"]),
            "--title",
            title,
            "--body-file",
            "-",
        ]
        for lb in add:
            cmd += ["--add-label", lb]
        for lb in remove:
            cmd += ["--remove-label", lb]
        gh(*cmd, input_text=body)
        updated += 1
        time.sleep(1.0)

    print(f"Issues: {created} creados, {updated} actualizados, {unchanged} sin cambios")
    return 0


if __name__ == "__main__":
    sys.exit(main())
