---
id: E10-02
title: "Tablero: trabajos por técnico"
epic: E10
phase: 1
priority: must
status: draft
roles: [owner, admin]
size: S
areas: [backend, web-admin]
depends_on: [E10-01]
blocked_by: []
assumes: []
---

# E10-02 Tablero: trabajos por técnico

## Historia

**Como** dirección, **quiero** ver cuántos trabajos hizo cada técnico en el período, **para** repartir mejor la carga.

## Criterios de aceptación

1. **Dado:** un período. **Cuando:** lo elijo. **Entonces:** veo por técnico las órdenes cerradas y en curso.
2. **Dado:** el tablero. **Cuando:** lo consulta un técnico. **Entonces:** recibe acceso denegado.
