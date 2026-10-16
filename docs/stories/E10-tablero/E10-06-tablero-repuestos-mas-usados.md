---
id: E10-06
title: "Tablero: repuestos más usados"
epic: E10
phase: 1
priority: must
status: draft
roles: [owner, admin]
size: S
areas: [backend, web-admin]
depends_on: [E10-01, E08-04]
blocked_by: []
assumes: []
---

# E10-06 Tablero: repuestos más usados

## Historia

**Como** dirección, **quiero** ver qué repuestos se usan más, **para** planificar compras y stock.

## Criterios de aceptación

1. **Dado:** usos de repuestos en el período. **Cuando:** abro la sección. **Entonces:** veo el ranking de repuestos por cantidad usada.
2. **Dado:** el ranking. **Cuando:** filtro por período, técnico o tipo de equipo. **Entonces:** se actualiza.
