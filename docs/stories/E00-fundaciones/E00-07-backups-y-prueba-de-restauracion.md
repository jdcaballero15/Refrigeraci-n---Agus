---
id: E00-07
title: "Backups y prueba de restauración"
epic: E00
phase: 1
priority: must
status: draft
roles: [dev]
size: S
areas: [infra]
depends_on: [E00-05]
blocked_by: []
assumes: []
---

# E00-07 Backups y prueba de restauración

## Historia

**Como** equipo de desarrollo, **quiero** backups diarios de la base y del bucket, con una prueba de restauración documentada, **para** no perder órdenes ni cobros ante un error o una caída.

## Criterios de aceptación

1. **Dado:** la base de producción. **Cuando:** pasa un día. **Entonces:** existe un backup nuevo y se conserva según la política definida.
2. **Dado:** un backup. **Cuando:** se restaura en un entorno aparte. **Entonces:** la aplicación arranca y los datos coinciden con el punto elegido.
3. **Dado:** la restauración. **Cuando:** se completa. **Entonces:** queda un procedimiento paso a paso en `docs/` con la fecha de la última prueba.
4. **Dado:** el bucket de archivos. **Cuando:** se borra un objeto por error. **Entonces:** se puede recuperar (versionado del bucket).

## Notas técnicas

- Repetir la prueba de restauración cada trimestre.
