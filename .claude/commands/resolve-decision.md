---
description: Registra la resolución de una decisión pendiente y desbloquea las historias afectadas
argument-hint: <ID de decisión, por ejemplo D-001> <resolución>
---

Registrá la resolución de **$ARGUMENTS**.

1. Leé la decisión en `docs/domain/decisiones-pendientes.md` y los ADR relacionados.
2. Actualizá su estado a `Resuelta`, con la resolución, quién la tomó y la fecha. No inventes la resolución: usá solo lo que te dije.
3. Buscá con `grep -r "blocked_by" docs/stories` las historias afectadas. Quitá el `blocked_by` correspondiente y, si ya no tienen otros bloqueos, listalas para que yo las pase a `ready` (no cambies el estado vos).
4. Si la resolución elimina historias (por ejemplo, el offline no hace falta), pasalas a `status: icebox` o `cancelled` y explicá por qué en su sección de notas.
5. Actualizá los ADR y documentos afectados (por ejemplo, ADR 0003 si es `D-001`).
6. Corré `make stories-validate` y mostrame un resumen de lo que cambió.
