---
id: E07-07
title: "Registrar mediciones y marcar las que están fuera de rango"
epic: E07
phase: 1
priority: must
status: draft
roles: [technician]
size: M
areas: [backend, pwa]
depends_on: [E07-06, E07-02]
blocked_by: []
assumes: []
---

# E07-07 Registrar mediciones y marcar las que están fuera de rango

## Historia

**Como** técnico, **quiero** cargar los valores medidos con la unidad ya puesta y que la app me avise si están fuera de rango, **para** detectar a tiempo un equipo que viene fallando.

## Criterios de aceptación

1. **Dado:** una tarea de medición. **Cuando:** ingreso un valor. **Entonces:** se acepta solo un número y se muestra la unidad y el rango esperado.
2. **Dado:** un valor fuera del rango. **Cuando:** lo ingreso. **Entonces:** la app lo marca y pide una observación obligatoria.
3. **Dado:** un valor dentro del rango. **Cuando:** lo ingreso. **Entonces:** no se pide nada más.
4. **Dado:** el cierre enviado. **Cuando:** el servidor lo procesa. **Entonces:** guarda el valor y si estuvo fuera de rango.
