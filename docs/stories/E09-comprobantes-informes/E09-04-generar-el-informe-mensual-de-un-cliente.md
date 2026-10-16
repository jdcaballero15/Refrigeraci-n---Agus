---
id: E09-04
title: "Generar el informe mensual de un cliente"
epic: E09
phase: 1
priority: must
status: draft
roles: [admin]
size: M
areas: [backend]
depends_on: [E04-06]
blocked_by: []
assumes: []
---

# E09-04 Generar el informe mensual de un cliente

## Historia

**Como** administración, **quiero** que el sistema arme el informe mensual de cada cliente con los trabajos realizados, **para** darle al cliente el historial sin construirle un portal.

## Criterios de aceptación

1. **Dado:** un cliente con trabajos en el mes. **Cuando:** se genera el informe. **Entonces:** lista cada trabajo con fecha, equipo, tipo, falla y reparación.
2. **Dado:** un cliente sin trabajos en el mes. **Cuando:** se genera. **Entonces:** no se envía informe vacío.
3. **Dado:** el informe. **Cuando:** se genera. **Entonces:** no incluye datos de otros clientes.
4. **Dado:** un mismo período. **Cuando:** se genera dos veces. **Entonces:** produce el mismo contenido.

## Preguntas abiertas

- ¿El informe muestra precios o importes? ¿Incluye las mediciones del mantenimiento?
