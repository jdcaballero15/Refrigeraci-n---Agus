---
id: E02-06
title: "Gestionar la lista de precios de repuestos"
epic: E02
phase: 1
priority: must
status: draft
roles: [admin]
size: M
areas: [backend, web-admin]
depends_on: [E02-05]
blocked_by: []
assumes: []
---

# E02-06 Gestionar la lista de precios de repuestos

## Historia

**Como** administración, **quiero** cargar y actualizar el precio de lista de cada repuesto conservando el historial, **para** calcular costos sin perder los precios con que se facturó antes.

## Criterios de aceptación

1. **Dado:** administración. **Cuando:** actualiza el precio de un repuesto. **Entonces:** se agrega un precio nuevo con fecha de vigencia y el anterior se conserva.
2. **Dado:** un precio actualizado. **Cuando:** hay órdenes ya cerradas con ese repuesto. **Entonces:** esas órdenes mantienen el precio estampado al usarlo.
3. **Dado:** el rol técnico. **Cuando:** consulta cualquier recurso de repuestos. **Entonces:** ningún campo de precio está en la respuesta.
4. **Dado:** un cambio de precio. **Cuando:** se guarda. **Entonces:** queda en la auditoría.

## Notas técnicas

- Tabla `part_price`. Los precios en pesos. Ver ADR 0005.
