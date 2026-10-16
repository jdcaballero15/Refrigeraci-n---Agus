---
id: E02-01
title: "Gestionar tipos de trabajo y tareas"
epic: E02
phase: 1
priority: must
status: draft
roles: [admin]
size: M
areas: [backend, web-admin]
depends_on: [E01-04]
blocked_by: []
assumes: [D-003]
---

# E02-01 Gestionar tipos de trabajo y tareas

## Historia

**Como** administración, **quiero** editar los tipos de trabajo (instalación, reparación, service, devolución, retiro, relevamiento) y sus subtareas, **para** estandarizar los términos sin depender de desarrollo.

## Criterios de aceptación

1. **Dado:** administración. **Cuando:** crea, renombra o desactiva un tipo de trabajo. **Entonces:** el cambio se ve en las órdenes nuevas y no altera las órdenes pasadas.
2. **Dado:** un tipo de trabajo. **Cuando:** administración le agrega subtareas. **Entonces:** aparecen como opciones al crear y cerrar órdenes de ese tipo.
3. **Dado:** un valor desactivado. **Cuando:** está en uso en órdenes existentes. **Entonces:** sigue mostrándose en ellas y no se ofrece en las nuevas.
4. **Dado:** un nombre duplicado. **Cuando:** se intenta guardar. **Entonces:** se rechaza.
5. **Dado:** un técnico. **Cuando:** intenta editar catálogos. **Entonces:** recibe acceso denegado.

## Notas técnicas

- Los seis tipos iniciales se cargan como datos semilla, y siguen siendo editables.
