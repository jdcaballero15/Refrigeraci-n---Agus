---
id: E00-03
title: "Base de la app del técnico como PWA instalable"
epic: E00
phase: 1
priority: must
status: ready
roles: [dev]
size: M
areas: [pwa, infra]
depends_on: []
blocked_by: []
assumes: []
---

# E00-03 Base de la app del técnico como PWA instalable

## Historia

**Como** equipo de desarrollo, **quiero** el esqueleto de `pwa-tecnico` como PWA instalable en Android, **para** entregar al técnico una app sin pasar por tiendas de aplicaciones.

## Criterios de aceptación

1. **Dado:** la app publicada en staging. **Cuando:** la abro en Chrome de Android. **Entonces:** puedo instalarla en la pantalla de inicio y abre a pantalla completa.
2. **Dado:** la app instalada. **Cuando:** abro sin conexión. **Entonces:** carga la carcasa de la aplicación desde el service worker.
3. **Dado:** una nueva versión desplegada. **Cuando:** el técnico abre la app con conexión. **Entonces:** se actualiza sin reinstalar y se le avisa si hay cambios pendientes de aplicar.
4. **Dado:** un cambio en `pwa-tecnico`. **Cuando:** se abre un PR. **Entonces:** CI corre lint, typecheck, tests y build.

## Notas técnicas

- La carcasa offline no depende de `D-001`: instalarse y abrir sin red es útil en cualquier caso. El almacenamiento de datos offline está en E05-09 a E05-11.
