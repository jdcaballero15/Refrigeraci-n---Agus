---
description: Crea una historia de usuario nueva en docs/stories/ con el formato del proyecto
argument-hint: <descripción de lo que se necesita>
---

Creá una historia nueva a partir de este pedido: **$ARGUMENTS**

1. Usá el subagente `story-writer`.
2. Leé `docs/stories/README.md` y `docs/stories/_template.md`.
3. Decidí la épica y el próximo ID libre de esa épica (revisá los archivos existentes).
4. Redactá la historia con criterios de aceptación verificables. Si algo no está en las fuentes, dejalo en "Preguntas abiertas" y no lo inventes.
5. Si depende de una decisión pendiente, agregá `blocked_by` y dejala en `status: draft`.
6. Corré `make stories-validate` y corregí los errores.
7. Mostrame la historia y qué preguntas necesitan respuesta de negocio.
