# ADR 0001: Monorepo

**Estado:** Aceptado

## Contexto

El sistema tiene backend, app de administración y app del técnico, que comparten contratos de API, reglas de dominio e historias. Hay pocas personas desarrollando y un solo cliente.

## Decisión

Un único repositorio (`backend/`, `web-admin/`, `pwa-tecnico/`, `docs/`) con CI por área mediante filtro de rutas y un único check requerido (`ci-ok`).

## Consecuencias

- Un PR puede cambiar API y clientes de forma atómica.
- Las historias, ADR y código viven juntos, y los agentes de IA ven todo el contexto.
- El CI debe filtrar por rutas para no correr todo siempre.
- Si en el futuro hace falta separar (por ejemplo, otro cliente con la misma app), se extrae un paquete, no se duplica el repo.
