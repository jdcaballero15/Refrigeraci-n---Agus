---
id: E04-06
title: "Detalle de la orden con línea de tiempo"
epic: E04
phase: 1
priority: must
status: draft
roles: [admin, owner]
size: M
areas: [backend, web-admin]
depends_on: [E04-01, E00-09]
blocked_by: []
assumes: []
---

# E04-06 Detalle de la orden con línea de tiempo

## Historia

**Como** administración, **quiero** ver el detalle completo de una orden con su línea de tiempo, **para** entender qué pasó, quién lo hizo y cuándo.

## Criterios de aceptación

1. **Dado:** una orden. **Cuando:** abro su detalle. **Entonces:** veo cliente, domicilio, equipo, tipo, técnico, estado y observaciones.
2. **Dado:** la línea de tiempo. **Cuando:** la consulto. **Entonces:** lista cada evento (creación, asignación, inicio, cierre, revisión, factura, cobro) con usuario y fecha.
3. **Dado:** una orden cerrada. **Cuando:** abro su detalle. **Entonces:** veo falla, reparación, repuestos usados con precio estampado, fotos y firma.
4. **Dado:** las fotos y la firma. **Cuando:** las abro. **Entonces:** se cargan con URLs firmadas de corta duración.
