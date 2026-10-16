---
id: E10-08
title: "Tablero: filtros por cliente, técnico, equipo y período"
epic: E10
phase: 1
priority: should
status: draft
roles: [owner, admin]
size: M
areas: [backend, web-admin]
depends_on: [E10-01]
blocked_by: []
assumes: []
---

# E10-08 Tablero: filtros por cliente, técnico, equipo y período

## Historia

**Como** dirección, **quiero** filtrar el tablero por cliente, técnico, equipo y período, y comparar entre meses, **para** analizar dónde se va el tiempo y la plata.

## Criterios de aceptación

1. **Dado:** cualquier sección del tablero. **Cuando:** aplico filtros. **Entonces:** todos los indicadores se recalculan con esos filtros.
2. **Dado:** dos períodos. **Cuando:** los comparo. **Entonces:** veo la diferencia entre ambos.
3. **Dado:** un filtro aplicado. **Cuando:** comparto la dirección web. **Entonces:** el filtro viaja en la URL.

## Notas técnicas

- Equivale a lo que daba la opción Power BI: filtros y comparación entre meses.
