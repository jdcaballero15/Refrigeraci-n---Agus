---
id: E04-07
title: "Cancelar una orden con motivo"
epic: E04
phase: 1
priority: must
status: draft
roles: [admin]
size: S
areas: [backend, web-admin]
depends_on: [E04-01]
blocked_by: []
assumes: []
---

# E04-07 Cancelar una orden con motivo

## Historia

**Como** administración, **quiero** cancelar una orden indicando el motivo, **para** sacar del circuito lo que ya no se hará sin borrar el registro.

## Criterios de aceptación

1. **Dado:** una orden `Pendiente`, `Asignada` o `En curso`. **Cuando:** administración la cancela con un motivo. **Entonces:** pasa a `Cancelada` y queda el motivo en el evento.
2. **Dado:** una cancelación sin motivo. **Cuando:** se intenta. **Entonces:** se rechaza.
3. **Dado:** una orden `Asignada` o `En curso`. **Cuando:** se cancela. **Entonces:** desaparece de la lista del técnico.
4. **Dado:** una orden `Terminada`, `Facturada` o `Cobrada`. **Cuando:** se intenta cancelar. **Entonces:** se rechaza.
5. **Dado:** una orden `En curso` con repuestos ya descontados del stock. **Cuando:** se cancela. **Entonces:** se informa y se ofrece revertir los movimientos con auditoría.

## Preguntas abiertas

- ¿Se puede cancelar una orden Terminada antes de facturar? La propuesta actual dice que no.
