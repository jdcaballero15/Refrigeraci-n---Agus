---
id: E02-05
title: "Gestionar el catálogo de repuestos"
epic: E02
phase: 1
priority: must
status: draft
roles: [admin]
size: M
areas: [backend, web-admin]
depends_on: [E01-04, E00-04]
blocked_by: []
assumes: [D-003]
---

# E02-05 Gestionar el catálogo de repuestos

## Historia

**Como** administración, **quiero** mantener el catálogo de repuestos con nombre y unidad, **para** que el técnico elija materiales de una lista y se sepa qué se usa.

## Criterios de aceptación

1. **Dado:** administración. **Cuando:** da de alta un repuesto con nombre y unidad. **Entonces:** queda disponible para los cierres y el stock.
2. **Dado:** un repuesto. **Cuando:** se guarda sin código. **Entonces:** es válido (hoy los repuestos no tienen código), y se puede agregar uno opcional.
3. **Dado:** un nombre muy parecido a uno existente. **Cuando:** se guarda. **Entonces:** el sistema advierte del posible duplicado.
4. **Dado:** un repuesto con movimientos o usos. **Cuando:** se quiere eliminar. **Entonces:** solo se puede desactivar.
5. **Dado:** el rol técnico. **Cuando:** consulta repuestos. **Entonces:** ve nombre y unidad y nunca el precio.

## Notas técnicas

- Entre 50 y 200 repuestos distintos.
