---
id: E02-02
title: "Gestionar tipos de equipo"
epic: E02
phase: 1
priority: must
status: draft
roles: [admin]
size: S
areas: [backend, web-admin]
depends_on: [E01-04]
blocked_by: []
assumes: [D-003]
---

# E02-02 Gestionar tipos de equipo

## Historia

**Como** administración, **quiero** editar los tipos de equipo (por ejemplo split, cámara frigorífica, heladera comercial), **para** clasificar equipos, fallas y checklists por tipo.

## Criterios de aceptación

1. **Dado:** administración. **Cuando:** crea o desactiva un tipo de equipo. **Entonces:** queda disponible o no al dar de alta equipos.
2. **Dado:** un tipo de equipo. **Cuando:** tiene equipos o checklists asociados. **Entonces:** no se puede borrar, solo desactivar.
3. **Dado:** un nombre duplicado. **Cuando:** se intenta guardar. **Entonces:** se rechaza.

## Preguntas abiertas

- ¿Cuál es la lista inicial de tipos de equipo? Se necesita del cliente.
