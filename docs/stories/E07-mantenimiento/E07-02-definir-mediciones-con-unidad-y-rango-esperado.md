---
id: E07-02
title: "Definir mediciones con unidad y rango esperado"
epic: E07
phase: 1
priority: must
status: draft
roles: [admin]
size: S
areas: [backend, web-admin]
depends_on: [E07-01]
blocked_by: []
assumes: []
---

# E07-02 Definir mediciones con unidad y rango esperado

## Historia

**Como** administración, **quiero** definir en una plantilla tareas de medición con su unidad (tensión, consumo, etc.) y un rango esperado, **para** detectar valores anormales en el momento.

## Criterios de aceptación

1. **Dado:** una plantilla. **Cuando:** agrego una tarea de tipo medición con unidad, mínimo y máximo. **Entonces:** el técnico ve la unidad ya puesta y el rango esperado.
2. **Dado:** un rango. **Cuando:** el mínimo es mayor que el máximo. **Entonces:** se rechaza.
3. **Dado:** una medición sin rango. **Cuando:** se guarda. **Entonces:** es válida y no se marca nunca fuera de rango.
