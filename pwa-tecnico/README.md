# pwa-tecnico

App del técnico. PWA instalable en celulares Android de la empresa. Pensada para una mano, con sol y guantes finos.

**Estado: sin crear.** El esqueleto lo crea la historia [E00-03](../docs/stories/E00-fundaciones/E00-03-base-de-la-app-del-tecnico-como-pwa-instalable.md). Hasta entonces el job de CI de esta carpeta se omite (no hay `package-lock.json`).

## Stack previsto

- React 18 y TypeScript estricto, Vite, `vite-plugin-pwa` (service worker y manifest).
- TanStack Query para datos del servidor.
- IndexedDB para la cola offline y las órdenes guardadas (solo si `D-001` confirma que hace falta, ver [ADR 0003](../docs/architecture/adr/0003-pwa-offline-first-provisional.md)).
- Firma en canvas, compresión de fotos en el cliente, subida directa al bucket con URL firmada.

## Qué hace (por épica)

| Épica | Funcionalidad |
|---|---|
| E05 | Mis órdenes, detalle, iniciar, cerrar con falla y reparación, repuestos, foto, observación, firma con nombre y DNI, resultado |
| E06 | Etapas de retiro, taller y devolución |
| E07 | Checklist de mantenimiento y mediciones |
| E05-09 a E05-11 | Modo offline y sincronización (bloqueadas por `D-001`) |

## Reglas

- **Nunca muestra ni guarda precios, mano de obra ni historial de clientes.** Solo usa lo que entrega la API `/tech/...`.
- Botones grandes (48 px o más), opciones predefinidas, casi sin escritura libre.
- Cada acción de escritura lleva una clave de idempotencia (UUID).
- Sin datos reales en capturas ni fixtures.
- Seguir `CLAUDE.md` y el agente `frontend-dev`.
