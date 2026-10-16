---
id: E10-04
title: "Tablero: avance del mantenimiento preventivo"
epic: E10
phase: 1
priority: must
status: draft
roles: [owner, admin]
size: S
areas: [backend, web-admin]
depends_on: [E10-01, E07-04]
blocked_by: []
assumes: []
---

# E10-04 Tablero: avance del mantenimiento preventivo

## Historia

**Como** dirección, **quiero** ver cuántas órdenes de mantenimiento del mes se generaron, se aprobaron y se cerraron, **para** saber si el preventivo va al día.

## Criterios de aceptación

1. **Dado:** una corrida mensual. **Cuando:** abro la sección. **Entonces:** veo generadas, aprobadas, asignadas, cerradas y pendientes.
2. **Dado:** un mes anterior. **Cuando:** lo elijo. **Entonces:** veo su avance final.
