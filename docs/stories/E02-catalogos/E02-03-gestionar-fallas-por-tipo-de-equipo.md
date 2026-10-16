---
id: E02-03
title: "Gestionar fallas por tipo de equipo"
epic: E02
phase: 1
priority: must
status: draft
roles: [admin]
size: M
areas: [backend, web-admin]
depends_on: [E02-02]
blocked_by: []
assumes: [D-003]
---

# E02-03 Gestionar fallas por tipo de equipo

## Historia

**Como** administración, **quiero** mantener el listado de fallas predefinidas por tipo de equipo, **para** que el técnico elija la falla de una lista y se pueda medir qué se rompe más.

## Criterios de aceptación

1. **Dado:** administración. **Cuando:** agrega una falla a un tipo de equipo. **Entonces:** el técnico la ve al cerrar órdenes de equipos de ese tipo.
2. **Dado:** una falla sin tipo de equipo. **Cuando:** se guarda. **Entonces:** aplica a todos los tipos.
3. **Dado:** la lista de fallas. **Cuando:** el técnico la ve. **Entonces:** siempre incluye la opción "Otro" que exige una observación.
4. **Dado:** una falla desactivada. **Cuando:** está en órdenes existentes. **Entonces:** se conserva en ellas.

## Preguntas abiertas

- Falta el listado de fallas más comunes por tipo de equipo (lo pidió la propuesta al cliente).
