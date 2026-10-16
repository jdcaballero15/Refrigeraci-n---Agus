---
id: E05-04
title: "Cerrar una orden con falla y reparación de listas"
epic: E05
phase: 1
priority: must
status: draft
roles: [technician]
size: M
areas: [backend, pwa]
depends_on: [E05-03, E02-03, E02-04]
blocked_by: []
assumes: []
---

# E05-04 Cerrar una orden con falla y reparación de listas

## Historia

**Como** técnico, **quiero** elegir la falla encontrada y la reparación realizada de listas predefinidas, **para** cerrar rápido, sin escribir, y dejar datos medibles.

## Criterios de aceptación

1. **Dado:** una orden `En curso` de un equipo. **Cuando:** abro el cierre. **Entonces:** veo las fallas del tipo de equipo y las reparaciones como botones o lista, no como texto libre.
2. **Dado:** la lista de fallas o reparaciones. **Cuando:** elijo "Otro". **Entonces:** la observación pasa a ser obligatoria.
3. **Dado:** un cierre sin falla o sin reparación elegidas. **Cuando:** intento enviarlo. **Entonces:** se marca qué falta.
4. **Dado:** los listados. **Cuando:** se cargan. **Entonces:** no incluyen precios ni datos de otros clientes.

## Preguntas abiertas

- ¿Qué datos de cierre aplican a instalación y relevamiento? Falla y reparación tienen sentido para reparación y service.
