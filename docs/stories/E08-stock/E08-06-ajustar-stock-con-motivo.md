---
id: E08-06
title: "Ajustar stock con motivo"
epic: E08
phase: 1
priority: should
status: draft
roles: [admin]
size: S
areas: [backend, web-admin]
depends_on: [E08-02]
blocked_by: []
assumes: []
---

# E08-06 Ajustar stock con motivo

## Historia

**Como** administración, **quiero** ajustar el stock de un repuesto indicando el motivo, **para** corregir diferencias de inventario sin pisar el historial.

## Criterios de aceptación

1. **Dado:** administración. **Cuando:** registra un ajuste con repuesto, ubicación, cantidad (positiva o negativa) y motivo obligatorio. **Entonces:** se agrega un movimiento `adjustment`.
2. **Dado:** un ajuste. **Cuando:** se registra. **Entonces:** queda en la auditoría.
3. **Dado:** un ajuste sin motivo. **Cuando:** se intenta. **Entonces:** se rechaza.
