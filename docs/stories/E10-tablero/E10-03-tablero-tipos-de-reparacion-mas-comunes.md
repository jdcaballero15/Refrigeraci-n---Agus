---
id: E10-03
title: "Tablero: tipos de reparación más comunes"
epic: E10
phase: 1
priority: must
status: draft
roles: [owner, admin]
size: S
areas: [backend, web-admin]
depends_on: [E10-01, E05-04]
blocked_by: []
assumes: []
---

# E10-03 Tablero: tipos de reparación más comunes

## Historia

**Como** dirección, **quiero** ver qué fallas y reparaciones son más frecuentes, por tipo de equipo, **para** entender qué se rompe más y qué se hace para solucionarlo.

## Criterios de aceptación

1. **Dado:** cierres con falla y reparación. **Cuando:** abro la sección. **Entonces:** veo el ranking de fallas y de reparaciones con cantidades.
2. **Dado:** el ranking. **Cuando:** filtro por tipo de equipo o período. **Entonces:** se actualiza.
3. **Dado:** los textos de "Otro". **Cuando:** hay muchos. **Entonces:** se muestran agrupados aparte para sugerir su promoción (E02-07).
