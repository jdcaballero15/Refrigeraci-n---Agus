---
id: E00-02
title: "Base de la app de administración"
epic: E00
phase: 1
priority: must
status: ready
roles: [dev]
size: S
areas: [web-admin, infra]
depends_on: []
blocked_by: []
assumes: []
---

# E00-02 Base de la app de administración

## Historia

**Como** equipo de desarrollo, **quiero** el esqueleto de `web-admin` con React, TypeScript y Vite, con lint, tests y build en CI, **para** empezar a construir pantallas de administración sobre una base común.

## Criterios de aceptación

1. **Dado:** el repositorio recién clonado. **Cuando:** corro `npm ci && npm run build` en `web-admin`. **Entonces:** compila sin errores.
2. **Dado:** un cambio en `web-admin`. **Cuando:** se abre un PR. **Entonces:** CI corre lint, typecheck, tests y build.
3. **Dado:** la API del backend. **Cuando:** se genera el cliente tipado desde OpenAPI. **Entonces:** el frontend usa los tipos generados y no tipos escritos a mano.
4. **Dado:** la app corriendo. **Cuando:** abro la ruta raíz. **Entonces:** veo una pantalla de inicio de sesión vacía en español.

## Notas técnicas

- Incluir `package-lock.json` para que el job de CI deje de omitirse.
- TanStack Query para datos del servidor. Estructura por funcionalidad, no por tipo de archivo.
