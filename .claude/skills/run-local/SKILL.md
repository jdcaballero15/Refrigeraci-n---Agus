---
name: run-local
description: Levanta el entorno local de OT Platform (base, bucket, mail de prueba y API) y comprueba que funciona. Usar cuando se pida correr, arrancar o probar la app localmente.
---

# Correr OT Platform en local

Todo corre en Docker Compose: `db` (Postgres 16), `minio` (bucket S3 compatible), `mailpit` (mail de prueba) y `backend`.

## Pasos

1. Copiar variables: `cp .env.example .env` (el `.env` no se commitea ni se lee desde los agentes).
2. Levantar: `make up`.
3. Ver logs: `make logs`.
4. Comprobar la API: `curl -s http://localhost:8000/health` debe responder `{"status":"ok"}`.
5. Documentación interactiva de la API: `http://localhost:8000/docs`.
6. Mail de prueba: `http://localhost:8025` (Mailpit). Bucket: consola de MinIO en `http://localhost:9001`.
7. Bajar: `make down`.

## Trampas conocidas

- **La base local usa el puerto 5433** (no el 5432) a propósito: así un Postgres instalado en la máquina no se confunde con el de Docker, un error difícil de detectar porque `localhost` responde igual. Desde el host: `postgresql+asyncpg://ot:ot@localhost:5433/ot`.
- **El `.env` no se carga solo** fuera de Docker. Si corrés `uvicorn` a mano: `set -a && source .env && set +a`.
- **Cambios en dependencias** (`pyproject.toml`) requieren `docker compose build backend`.
- Datos de prueba siempre ficticios. Nunca cargar una exportación real de Persat.

Si algo de esto falla distinto, anotarlo acá: este archivo se actualiza con cada trampa nueva.
