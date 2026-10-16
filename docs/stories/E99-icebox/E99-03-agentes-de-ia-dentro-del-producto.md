---
id: E99-03
title: "Agentes de IA dentro del producto"
epic: E99
phase: 2
priority: could
status: icebox
roles: [admin]
size: L
areas: [backend, web-admin]
depends_on: []
blocked_by: []
assumes: []
---

# E99-03 Agentes de IA dentro del producto

## Historia

**Como** administración, **quiero** resúmenes del historial de un equipo y sugerencias de falla a partir de las observaciones, **para** ahorrar tiempo de lectura y mejorar la estandarización.

## Criterios de aceptación

1. **Dado:** un equipo con historial largo. **Cuando:** administración pide un resumen. **Entonces:** recibe un resumen con enlaces a las órdenes de origen.
2. **Dado:** una observación en "Otro". **Cuando:** se revisa. **Entonces:** el sistema sugiere la falla del catálogo más parecida y administración decide.

## Notas técnicas

- Ver ADR 0008. Cualquier uso de IA con datos de clientes exige revisar `D-008` y no enviar DNI ni firmas a terceros.
