---
description: Implementa una historia de docs/stories/ de punta a punta (rama, tests, código, PR)
argument-hint: <ID de la historia, por ejemplo E04-03>
---

Implementá la historia **$ARGUMENTS**.

1. Buscá el archivo en `docs/stories/` y leelo completo, junto con los documentos que referencia.
2. Verificá que tenga `status: ready` y ningún `blocked_by` abierto en `docs/domain/decisiones-pendientes.md`. Si no se cumple, frená y explicá por qué. No implementes nada.
3. Si hay preguntas abiertas o contradicciones, listalas y preguntame antes de seguir.
4. Elegí el subagente según el área (`backend-dev`, `frontend-dev`, `db-migrations`) y trabajá en una rama `feat/$ARGUMENTS-<descripcion-corta>`.
5. Tests primero: uno por criterio de aceptación.
6. Implementá respetando `CLAUDE.md`. Corré `make lint` y `make test`.
7. Revisá el resultado con el subagente `qa-reviewer` y corregí lo bloqueante.
8. Actualizá la historia (`status: done`, notas técnicas) y los documentos que cambien.
9. Hacé commits con Conventional Commits y dejá el PR listo con la plantilla completa. **No hagas merge.**

Al final, resumí qué criterios cubriste, qué quedó pendiente y qué decisiones tomaste.
