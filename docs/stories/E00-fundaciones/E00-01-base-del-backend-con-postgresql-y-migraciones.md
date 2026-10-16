---
id: E00-01
title: "Base del backend con PostgreSQL y migraciones"
epic: E00
phase: 1
priority: must
status: ready
roles: [dev]
size: S
areas: [backend, infra]
depends_on: []
blocked_by: []
assumes: []
---

# E00-01 Base del backend con PostgreSQL y migraciones

## Historia

**Como** equipo de desarrollo, **quiero** un backend con conexión asíncrona a PostgreSQL y Alembic configurados, **para** construir los módulos sobre una base común.

## Criterios de aceptación

1. **Dado:** el entorno local levantado con `make up`. **Cuando:** consulto `GET /health/ready`. **Entonces:** la respuesta indica que la base responde.
2. **Dado:** una base vacía. **Cuando:** corro `alembic upgrade head`. **Entonces:** se crea el esquema inicial sin errores y `alembic downgrade base` lo deshace.
3. **Dado:** el modelo base. **Cuando:** se crea cualquier tabla. **Entonces:** incluye `id` (uuid), `created_at`, `updated_at` y `deleted_at`.
4. **Dado:** un repositorio base. **Cuando:** consulto registros. **Entonces:** excluye por defecto los que tienen `deleted_at`.

## Notas técnicas

- Capas y convenciones en `backend/README.md`. El repositorio base es el único lugar que filtra `deleted_at`.
- En CI las pruebas usan el servicio Postgres del workflow.
