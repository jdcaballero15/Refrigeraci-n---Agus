---
id: E02-04
title: "Gestionar reparaciones"
epic: E02
phase: 1
priority: must
status: draft
roles: [admin]
size: S
areas: [backend, web-admin]
depends_on: [E02-02]
blocked_by: []
assumes: [D-003]
---

# E02-04 Gestionar reparaciones

## Historia

**Como** administración, **quiero** mantener el listado de reparaciones predefinidas, **para** que el técnico elija la reparación realizada de una lista.

## Criterios de aceptación

1. **Dado:** administración. **Cuando:** agrega una reparación. **Entonces:** el técnico la ve al cerrar una orden.
2. **Dado:** la lista de reparaciones. **Cuando:** el técnico la ve. **Entonces:** incluye "Otro" con observación obligatoria.
3. **Dado:** una reparación desactivada. **Cuando:** está en órdenes existentes. **Entonces:** se conserva en ellas.
