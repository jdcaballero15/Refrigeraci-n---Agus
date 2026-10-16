---
id: E05-01
title: "Ver mis órdenes asignadas"
epic: E05
phase: 1
priority: must
status: draft
roles: [technician]
size: S
areas: [backend, pwa]
depends_on: [E04-03, E01-04, E00-03]
blocked_by: []
assumes: []
---

# E05-01 Ver mis órdenes asignadas

## Historia

**Como** técnico, **quiero** ver la lista de mis órdenes asignadas con cliente, dirección, equipo y tarea, **para** saber a dónde ir y qué hacer.

## Criterios de aceptación

1. **Dado:** un técnico con órdenes asignadas. **Cuando:** abre la app. **Entonces:** ve solo sus órdenes `Asignada` y `En curso`, ordenadas por fecha prevista.
2. **Dado:** una orden reasignada o cancelada. **Cuando:** el técnico actualiza la lista. **Entonces:** deja de verla.
3. **Dado:** la respuesta de la API. **Cuando:** se la inspecciona. **Entonces:** no contiene precios, mano de obra ni historial de clientes.
4. **Dado:** un técnico sin órdenes. **Cuando:** abre la app. **Entonces:** ve un mensaje claro de que no tiene trabajo asignado.

## Notas técnicas

- Endpoint `/tech/orders`. Esquema `OrderTechnicianOut`. Cubierto por el test de contrato E00-04.
