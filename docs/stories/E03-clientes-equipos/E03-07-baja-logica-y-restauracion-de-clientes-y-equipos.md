---
id: E03-07
title: "Baja lógica y restauración de clientes y equipos"
epic: E03
phase: 1
priority: should
status: draft
roles: [admin]
size: S
areas: [backend, web-admin]
depends_on: [E03-01, E03-03]
blocked_by: []
assumes: []
---

# E03-07 Baja lógica y restauración de clientes y equipos

## Historia

**Como** administración, **quiero** dar de baja y restaurar clientes y equipos, **para** corregir errores sin perder información.

## Criterios de aceptación

1. **Dado:** un cliente o equipo. **Cuando:** administración lo da de baja. **Entonces:** deja de ofrecerse para órdenes nuevas y conserva todo su historial.
2. **Dado:** un registro dado de baja. **Cuando:** administración lo restaura. **Entonces:** vuelve a estar disponible.
3. **Dado:** una baja o restauración. **Cuando:** se realiza. **Entonces:** queda en la auditoría.
4. **Dado:** un cliente con órdenes abiertas. **Cuando:** se intenta dar de baja. **Entonces:** el sistema lo impide e indica las órdenes.
