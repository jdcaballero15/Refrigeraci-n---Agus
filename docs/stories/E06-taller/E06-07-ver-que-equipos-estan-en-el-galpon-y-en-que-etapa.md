---
id: E06-07
title: "Ver qué equipos están en el galpón y en qué etapa"
epic: E06
phase: 1
priority: must
status: draft
roles: [admin, owner]
size: S
areas: [backend, web-admin]
depends_on: [E06-04]
blocked_by: []
assumes: []
---

# E06-07 Ver qué equipos están en el galpón y en qué etapa

## Historia

**Como** administración, **quiero** ver la lista de equipos que están en el galpón y en qué etapa está cada uno, **para** saber qué hay en el taller y qué falta devolver.

## Criterios de aceptación

1. **Dado:** órdenes de taller con retiro completado y devolución pendiente. **Cuando:** abro la vista. **Entonces:** listo esos equipos con cliente, equipo, etapa actual y técnico.
2. **Dado:** la vista. **Cuando:** filtro por cliente o etapa. **Entonces:** se actualiza.
3. **Dado:** un equipo devuelto. **Cuando:** se completa la devolución. **Entonces:** deja de aparecer en la vista.
4. **Dado:** el rol técnico. **Cuando:** intenta acceder. **Entonces:** recibe acceso denegado.
