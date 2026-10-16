---
id: E03-03
title: "Alta y edición de equipos"
epic: E03
phase: 1
priority: must
status: draft
roles: [admin]
size: M
areas: [backend, web-admin]
depends_on: [E03-02, E02-02]
blocked_by: [D-002]
assumes: []
---

# E03-03 Alta y edición de equipos

## Historia

**Como** administración, **quiero** dar de alta y editar los equipos de un cliente, **para** tener el parque de equipos para asociar trabajos e historial.

## Criterios de aceptación

1. **Dado:** administración. **Cuando:** crea un equipo con tipo, domicilio y marca o modelo. **Entonces:** queda asociado al cliente y disponible para órdenes.
2. **Dado:** el esquema de identificación decidido en `D-002`. **Cuando:** se carga un equipo. **Entonces:** se exige el identificador que corresponda (código propio o ubicación dentro del cliente).
3. **Dado:** un equipo. **Cuando:** se quiere eliminar. **Entonces:** solo se puede dar de baja lógica y conserva su historial.
4. **Dado:** un identificador duplicado dentro del cliente. **Cuando:** se guarda. **Entonces:** se rechaza.

## Notas técnicas

- El modelo tiene `internal_code` y `location_note` opcionales hasta resolver `D-002`. Entre 200 y 1.000 equipos.
