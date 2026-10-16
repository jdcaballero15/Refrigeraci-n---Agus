# Ciclo de una historia con tres puertas

Adaptado del flujo AI-DLC de otro repositorio de MendoData. Sirve igual para personas y para agentes.
Tres puertas reales de frenado y nada más. Entre puertas se trabaja sin pedir permiso.

| Puerta | Cuándo | Quién aprueba | Qué se revisa |
|---|---|---|---|
| 1. Plan | Antes de escribir código | Quien pidió el trabajo (Juan Diego o Gonza) | Historia en `ready` sin `blocked_by`, archivos a tocar, tests a escribir, ADR necesario |
| 2. Verificación | Después de implementar | Quien implementa muestra la salida real | `make lint`, `make test`, validador de historias, sin secretos |
| 3. Pull Request | Recién cuando se pide | Revisión humana más CI `ci-ok` | Plantilla completa, Definición de Terminado |

Reglas:

- La puerta es un freno real. Nunca se infiere aprobación del silencio.
- `CLAUDE.md` manda sobre este flujo. Si un plan solo se puede ejecutar rompiendo una regla, el plan está mal: se frena y se vuelve a planificar.
- Las preguntas se hacen en el momento y la respuesta queda en el plan, no en archivos aparte.
- Cambio tan chico que el plan sería más largo que el diff (un typo, un texto): se dice en una línea y se hace, igual en una rama y con PR.
- Si una historia está en `draft` o bloqueada, el problema es la historia: se frena y se avisa.

## Plan de la unidad (puerta 1)

Un párrafo por punto, en el comentario del issue o en el primer mensaje del PR:

1. Historia (`EXX-NN`) y criterios de aceptación que cubre.
2. Archivos y capas que se tocan.
3. Tests que se escriben primero.
4. Migraciones o ADR necesarios.
5. Riesgos y decisiones pendientes que rozan la historia.
