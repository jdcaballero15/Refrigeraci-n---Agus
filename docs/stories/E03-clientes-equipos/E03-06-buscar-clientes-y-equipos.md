---
id: E03-06
title: "Buscar clientes y equipos"
epic: E03
phase: 1
priority: must
status: draft
roles: [admin, owner]
size: S
areas: [backend, web-admin]
depends_on: [E03-01]
blocked_by: []
assumes: []
---

# E03-06 Buscar clientes y equipos

## Historia

**Como** administración, **quiero** buscar clientes y equipos por nombre, dirección o identificador, **para** encontrar rápido a quién me llama por teléfono.

## Criterios de aceptación

1. **Dado:** un texto de búsqueda. **Cuando:** busco. **Entonces:** obtengo coincidencias de clientes y equipos tolerando mayúsculas, acentos y errores menores.
2. **Dado:** miles de registros. **Cuando:** busco. **Entonces:** la respuesta tarda menos de 500 ms en el entorno de producción.
3. **Dado:** un registro dado de baja. **Cuando:** busco. **Entonces:** no aparece salvo que active "ver bajas".

## Notas técnicas

- Postgres con `pg_trgm` y `unaccent`. Sin límites de delegación como en Power Apps.
