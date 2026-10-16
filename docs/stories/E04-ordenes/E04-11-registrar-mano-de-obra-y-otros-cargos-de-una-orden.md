---
id: E04-11
title: "Registrar mano de obra y otros cargos de una orden"
epic: E04
phase: 1
priority: should
status: draft
roles: [admin]
size: M
areas: [backend, web-admin]
depends_on: [E04-06, E00-04]
blocked_by: []
assumes: []
---

# E04-11 Registrar mano de obra y otros cargos de una orden

## Historia

**Como** administración, **quiero** registrar la mano de obra y otros cargos de una orden y ver el total junto con los repuestos, **para** preparar la facturación con los importes correctos.

## Criterios de aceptación

1. **Dado:** una orden cerrada. **Cuando:** administración agrega un cargo (mano de obra, visita u otro) con concepto e importe. **Entonces:** se guarda como un registro de cargo con usuario y fecha.
2. **Dado:** una orden con repuestos usados. **Cuando:** administración ve el total. **Entonces:** suma los repuestos al precio estampado y los cargos registrados.
3. **Dado:** el rol técnico. **Cuando:** consulta cualquier orden. **Entonces:** no hay ningún cargo, importe ni total en la respuesta.
4. **Dado:** un cargo. **Cuando:** se edita o se anula. **Entonces:** queda en la auditoría.

## Preguntas abiertas

- La propuesta no describe cómo se calcula la mano de obra. Hay precios por lista general, abono mensual y presupuesto por trabajo: se necesita el criterio para cada caso.
- Está ligado a `D-004` (qué datos necesita administración para facturar).
