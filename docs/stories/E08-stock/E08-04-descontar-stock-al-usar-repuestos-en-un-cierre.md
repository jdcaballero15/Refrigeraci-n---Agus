---
id: E08-04
title: "Descontar stock al usar repuestos en un cierre"
epic: E08
phase: 1
priority: must
status: draft
roles: [technician]
size: M
areas: [backend]
depends_on: [E08-03, E05-12, E02-06]
blocked_by: []
assumes: []
---

# E08-04 Descontar stock al usar repuestos en un cierre

## Historia

**Como** técnico, **quiero** que al cerrar una orden con repuestos se descuente el stock de mi camioneta, **para** no tener que cargar el consumo dos veces.

## Criterios de aceptación

1. **Dado:** un cierre con repuestos. **Cuando:** el servidor lo procesa. **Entonces:** crea un movimiento `usage` por repuesto desde la camioneta del técnico, en la misma transacción que el cierre.
2. **Dado:** un cierre. **Cuando:** se procesa dos veces por un reintento. **Entonces:** el stock se descuenta una sola vez (idempotencia).
3. **Dado:** un uso de repuesto. **Cuando:** se registra. **Entonces:** guarda el precio de lista vigente como precio estampado.
4. **Dado:** el técnico. **Cuando:** consulta su stock. **Entonces:** ve cantidades de su camioneta y no ve precios.
