---
id: E03-04
title: "Ficha de cliente con historial"
epic: E03
phase: 1
priority: must
status: draft
roles: [admin, owner]
size: M
areas: [backend, web-admin]
depends_on: [E03-01, E04-06]
blocked_by: []
assumes: []
---

# E03-04 Ficha de cliente con historial

## Historia

**Como** administración, **quiero** ver la ficha de un cliente con todos sus trabajos y repuestos usados, **para** responder consultas y decidir con el historial a la vista.

## Criterios de aceptación

1. **Dado:** un cliente con órdenes. **Cuando:** abro su ficha. **Entonces:** veo sus órdenes ordenadas por fecha con estado, tipo, equipo y técnico.
2. **Dado:** la ficha. **Cuando:** selecciono una orden. **Entonces:** veo falla, reparación, repuestos usados y observación.
3. **Dado:** un historial largo. **Cuando:** lo recorro. **Entonces:** está paginado y filtra por equipo, tipo de trabajo y período.
4. **Dado:** el rol técnico. **Cuando:** intenta acceder a la ficha. **Entonces:** recibe acceso denegado.

## Notas técnicas

- Es el "historial por cliente" que pidió la reunión original. Para administración y dirección, nunca para técnico.
