---
id: E07-06
title: "Completar el checklist de mantenimiento en la app del técnico"
epic: E07
phase: 1
priority: must
status: draft
roles: [technician]
size: M
areas: [backend, pwa]
depends_on: [E07-04, E05-03]
blocked_by: []
assumes: []
---

# E07-06 Completar el checklist de mantenimiento en la app del técnico

## Historia

**Como** técnico, **quiero** completar el checklist de la orden marcando cada tarea como OK o No OK, **para** registrar el mantenimiento sin escribir.

## Criterios de aceptación

1. **Dado:** una orden de mantenimiento `En curso`. **Cuando:** abro el cierre. **Entonces:** veo el checklist de su plantilla con botones OK y No OK por tarea.
2. **Dado:** un checklist con tareas sin responder. **Cuando:** intento enviar. **Entonces:** se marca cuáles faltan.
3. **Dado:** un ítem en No OK. **Cuando:** lo marco. **Entonces:** puedo agregar una observación.
4. **Dado:** la pantalla. **Cuando:** se inspecciona. **Entonces:** no incluye precios, mano de obra ni historial.
