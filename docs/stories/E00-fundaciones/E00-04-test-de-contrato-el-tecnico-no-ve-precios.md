---
id: E00-04
title: "Test de contrato: el técnico no ve precios"
epic: E00
phase: 1
priority: must
status: ready
roles: [dev]
size: S
areas: [backend]
depends_on: [E00-01]
blocked_by: []
assumes: []
---

# E00-04 Test de contrato: el técnico no ve precios

## Historia

**Como** equipo de desarrollo, **quiero** un test automático que recorra los esquemas de respuesta del técnico y falle si aparece un campo de precio, mano de obra o historial, **para** garantizar que la regla de visibilidad no se rompe sin que nadie lo note.

## Criterios de aceptación

1. **Dado:** los esquemas `*TechnicianOut`. **Cuando:** corre el test de contrato. **Entonces:** falla si algún campo (a cualquier profundidad) coincide con la lista de campos prohibidos.
2. **Dado:** la lista de campos prohibidos. **Cuando:** se agrega un campo nuevo sensible. **Entonces:** se edita en un solo archivo versionado y el test lo toma.
3. **Dado:** una ruta bajo `/tech/`. **Cuando:** la ruta devuelve un esquema que no termina en `TechnicianOut`. **Entonces:** el test falla.
4. **Dado:** el workflow de CI. **Cuando:** el test de contrato falla. **Entonces:** el check `ci-ok` queda en rojo.

## Notas técnicas

- Ver ADR 0006. Campos prohibidos iniciales: `price`, `unit_price`, `list_price`, `amount`, `charge`, `total`, y todo lo bajo `history`.
- También debe cubrir los esquemas de error, para que no filtren datos.
