---
id: E07-05
title: "Aprobar en bloque las órdenes de mantenimiento generadas"
epic: E07
phase: 1
priority: must
status: draft
roles: [admin]
size: M
areas: [backend, web-admin]
depends_on: [E07-04, E04-07]
blocked_by: []
assumes: [D-005]
---

# E07-05 Aprobar en bloque las órdenes de mantenimiento generadas

## Historia

**Como** administración, **quiero** revisar y aprobar de una vez las órdenes de mantenimiento generadas en el mes, **para** controlar lo que se va a enviar a campo sin aprobar una por una.

## Criterios de aceptación

1. **Dado:** órdenes generadas pendientes de aprobación. **Cuando:** administración abre la corrida del mes. **Entonces:** ve todas con cliente, equipo, tipo y checklist.
2. **Dado:** una selección de órdenes. **Cuando:** administración aprueba en bloque. **Entonces:** dejan de requerir aprobación y quedan disponibles para asignar.
3. **Dado:** una orden que no corresponde. **Cuando:** administración la descarta con motivo. **Entonces:** pasa a `Cancelada` y queda el motivo.
4. **Dado:** la aprobación. **Cuando:** se realiza. **Entonces:** queda registrada con usuario y fecha en la corrida.
