---
id: E07-04
title: "Generar las órdenes de mantenimiento cada mes"
epic: E07
phase: 1
priority: must
status: draft
roles: [admin]
size: L
areas: [backend]
depends_on: [E07-03, E00-11, E04-02]
blocked_by: []
assumes: [D-005]
---

# E07-04 Generar las órdenes de mantenimiento cada mes

## Historia

**Como** administración, **quiero** que todos los meses el sistema genere una orden por equipo de cada abonado, con el checklist que corresponde, **para** no crear a mano decenas de órdenes (hoy son unos 60 equipos en dos días).

## Criterios de aceptación

1. **Dado:** el primer día del mes a la hora configurada. **Cuando:** corre el job. **Entonces:** genera una orden `source = maintenance` por cada equipo vigente cuya frecuencia corresponde a ese mes.
2. **Dado:** el job. **Cuando:** se ejecuta dos veces para el mismo período. **Entonces:** no duplica órdenes (período único por corrida).
3. **Dado:** las órdenes generadas. **Cuando:** se crean. **Entonces:** quedan `Pendiente` con `requires_approval = true` y con el checklist de su plantilla.
4. **Dado:** un equipo sin plantilla aplicable. **Cuando:** se genera. **Entonces:** se omite y se informa a administración en el resumen de la corrida.
5. **Dado:** una corrida. **Cuando:** termina. **Entonces:** queda un resumen: cuántas se generaron, cuántas se omitieron y por qué.

## Preguntas abiertas

- ¿Cómo se define el mes en que corresponden los mantenimientos semestrales y anuales? Se propone usar el mes de la fecha de inicio del equipo en el abono.
