---
id: E07-01
title: "Gestionar plantillas de checklist por frecuencia y tipo de equipo"
epic: E07
phase: 1
priority: must
status: draft
roles: [admin]
size: M
areas: [backend, web-admin]
depends_on: [E02-02, E01-04]
blocked_by: []
assumes: []
---

# E07-01 Gestionar plantillas de checklist por frecuencia y tipo de equipo

## Historia

**Como** administración, **quiero** crear y editar plantillas de checklist por frecuencia (mensual, semestral, anual) y, si hace falta, por tipo de equipo, **para** que cada orden de mantenimiento llegue al técnico con las tareas que corresponden.

## Criterios de aceptación

1. **Dado:** administración. **Cuando:** crea una plantilla con frecuencia y tareas ordenadas. **Entonces:** queda disponible para generar órdenes de esa frecuencia.
2. **Dado:** una plantilla para un tipo de equipo. **Cuando:** existe también una general de la misma frecuencia. **Entonces:** se usa la del tipo de equipo para esos equipos y la general para el resto.
3. **Dado:** una plantilla editada. **Cuando:** hay órdenes ya generadas con la versión anterior. **Entonces:** esas órdenes conservan las tareas con que se generaron.
4. **Dado:** una tarea de plantilla. **Cuando:** se quita. **Entonces:** se desactiva, no se borra.
5. **Dado:** el rol técnico. **Cuando:** intenta editar plantillas. **Entonces:** recibe acceso denegado.

## Preguntas abiertas

- Falta el material de los checklists que usan hoy, de cada frecuencia (lo pidió la propuesta al cliente).
