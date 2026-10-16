---
id: E12-01
title: "Auditoría de cambios"
epic: E12
phase: 1
priority: must
status: draft
roles: [admin, owner]
size: M
areas: [backend, web-admin]
depends_on: [E00-01]
blocked_by: []
assumes: []
---

# E12-01 Auditoría de cambios

## Historia

**Como** dirección, **quiero** que los cambios sobre órdenes, catálogos, precios, stock y usuarios queden registrados con quién, cuándo y qué cambió, **para** saber qué pasó ante una duda o un error.

## Criterios de aceptación

1. **Dado:** una entidad auditada. **Cuando:** se crea, modifica o se da de baja. **Entonces:** se agrega un registro en `audit_log` con usuario, fecha, entidad, acción y diferencias.
2. **Dado:** dirección o administración. **Cuando:** consulta la auditoría. **Entonces:** puede filtrar por entidad, usuario y fecha.
3. **Dado:** el registro de auditoría. **Cuando:** se consulta. **Entonces:** no se puede editar ni borrar desde la aplicación.
4. **Dado:** los datos personales (DNI). **Cuando:** aparecen en una diferencia. **Entonces:** se enmascaran.
