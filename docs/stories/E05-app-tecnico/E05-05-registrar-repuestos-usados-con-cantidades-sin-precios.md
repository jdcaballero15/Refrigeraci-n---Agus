---
id: E05-05
title: "Registrar repuestos usados con cantidades, sin precios"
epic: E05
phase: 1
priority: must
status: draft
roles: [technician]
size: M
areas: [backend, pwa]
depends_on: [E05-04, E02-06, E08-04]
blocked_by: []
assumes: []
---

# E05-05 Registrar repuestos usados con cantidades, sin precios

## Historia

**Como** técnico, **quiero** elegir del catálogo los repuestos usados y cargar las cantidades, **para** que el stock y el costo del trabajo queden registrados sin que yo vea precios.

## Criterios de aceptación

1. **Dado:** un cierre en curso. **Cuando:** agrego un repuesto y una cantidad. **Entonces:** elijo de una lista con búsqueda y veo solo nombre y unidad.
2. **Dado:** el cierre enviado. **Cuando:** el servidor lo procesa. **Entonces:** estampa el precio vigente de cada repuesto en `part_usage.unit_price`.
3. **Dado:** el cierre enviado. **Cuando:** el servidor lo procesa. **Entonces:** descuenta el stock de la camioneta del técnico (ver E08-04).
4. **Dado:** una cantidad cero, negativa o no numérica. **Cuando:** intento agregarla. **Entonces:** se rechaza.
5. **Dado:** la app y la API del técnico. **Cuando:** se inspeccionan. **Entonces:** no exponen ningún precio.
