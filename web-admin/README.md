# web-admin

App de administración y tablero. Uso principal en PC o tablet, con el tablero también usable desde el celular (dirección).

**Estado: sin crear.** El esqueleto lo crea la historia [E00-02](../docs/stories/E00-fundaciones/E00-02-base-de-la-app-de-administracion.md). Hasta entonces el job de CI de esta carpeta se omite (no hay `package-lock.json`).

## Stack previsto

- React 18 y TypeScript estricto, Vite.
- TanStack Query para datos del servidor. Cliente de API generado desde el OpenAPI del backend.
- Estructura por funcionalidad (`src/features/orders`, `src/features/catalogs`, etc.), no por tipo de archivo.
- ESLint, Prettier, Vitest y Testing Library.

## Pantallas (por épica)

| Épica | Pantallas |
|---|---|
| E04 | Panel de órdenes, alta de orden, detalle con línea de tiempo, revisión, facturación y cobro |
| E03 | Clientes, equipos, fichas con historial |
| E02 | Catálogos y precios |
| E06 | Equipos en el galpón |
| E07 | Plantillas de checklist, abonos, aprobación en bloque |
| E08 | Stock, transferencias, movimientos |
| E10 | Tablero |
| E01 y E12 | Usuarios y auditoría |

## Reglas

- Interfaz en español, densa y eficiente para escritorio.
- Acciones sensibles con confirmación.
- Sin datos reales en capturas ni fixtures.
- Seguir `CLAUDE.md` y el agente `frontend-dev`.
