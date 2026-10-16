# ADR 0002: Backend con FastAPI y PostgreSQL

**Estado:** Aceptado

## Contexto

Se pasa de Power Apps con listas de SharePoint a un sistema a medida. Las limitaciones que se dejan atrás son los límites de delegación y el umbral de vista de listas, la falta de transacciones y las reglas de negocio repartidas entre flujos.

## Decisión

- Python 3.12 con FastAPI (tipado con Pydantic, documentación OpenAPI automática).
- PostgreSQL 16 como única base de datos.
- SQLAlchemy 2 asíncrono y Alembic para migraciones.
- Autenticación con JWT de corta duración y refresco, hash de contraseñas con Argon2 (detalle en la historia E01-01 y en `D-007`).

## Alternativas descartadas

- Java con Spring Boot: más verboso para el tamaño del sistema.
- NestJS: un solo lenguaje con el frontend, pero menos soporte para trabajo de datos y reportes que el equipo ya domina en Python.

## Consecuencias

- Transacciones reales para las operaciones críticas (cerrar orden y descontar stock).
- El contrato de la API se genera desde el código, y de él se pueden generar los tipos del frontend.
- Los reportes y el tablero se resuelven con SQL.
