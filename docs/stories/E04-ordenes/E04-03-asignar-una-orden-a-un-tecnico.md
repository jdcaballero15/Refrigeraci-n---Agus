---
id: E04-03
title: "Asignar una orden a un técnico"
epic: E04
phase: 1
priority: must
status: draft
roles: [admin]
size: S
areas: [backend, web-admin]
depends_on: [E04-02, E01-03]
blocked_by: []
assumes: []
---

# E04-03 Asignar una orden a un técnico

## Historia

**Como** administración, **quiero** asignar una orden pendiente a un técnico con una fecha prevista, **para** que el técnico la vea en su celular y sepa cuándo ir.

## Criterios de aceptación

1. **Dado:** una orden `Pendiente`. **Cuando:** administración la asigna a un técnico activo con fecha prevista. **Entonces:** pasa a `Asignada` y aparece en la lista de ese técnico.
2. **Dado:** una orden con aprobación pendiente (`requires_approval`). **Cuando:** se intenta asignar. **Entonces:** se rechaza hasta que se apruebe el lote.
3. **Dado:** un técnico dado de baja. **Cuando:** se intenta asignarle una orden. **Entonces:** no aparece como opción.
4. **Dado:** una asignación. **Cuando:** se realiza. **Entonces:** queda un evento con quién asignó, a quién y para qué fecha.
5. **Dado:** el técnico asignado. **Cuando:** ve la orden. **Entonces:** cumple las reglas de visibilidad (sin precios ni historial).

## Preguntas abiertas

- ¿Se asigna solo por día o también por franja horaria? (No hay registro de hora de llegada y salida, eso está fuera de alcance.)
