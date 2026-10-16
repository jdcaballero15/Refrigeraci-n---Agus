---
description: Crea y prueba una migración de Alembic siguiendo las reglas de datos
argument-hint: <descripción del cambio de base de datos>
---

Preparé una migración para: **$ARGUMENTS**

1. Usá el subagente `db-migrations`.
2. Actualizá primero `docs/architecture/data-model.dbml` (y un ADR si la decisión es nueva).
3. Generá la migración con `alembic revision --autogenerate -m "<descripcion>"` y revisala a mano.
4. Verificá las reglas: `deleted_at`, fechas y precios en tablas de transacción, nada de archivos en la base, índices necesarios.
5. Escribí `downgrade` y probá `upgrade head`, `downgrade -1`, `upgrade head` sobre una base limpia.
6. Informá el resultado y los archivos tocados. No hagas commit hasta que te lo pida.
