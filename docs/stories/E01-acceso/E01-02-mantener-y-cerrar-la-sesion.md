---
id: E01-02
title: "Mantener y cerrar la sesión"
epic: E01
phase: 1
priority: must
status: draft
roles: [admin, technician, owner]
size: S
areas: [backend, web-admin, pwa]
depends_on: [E01-01]
blocked_by: []
assumes: []
---

# E01-02 Mantener y cerrar la sesión

## Historia

**Como** usuario del sistema, **quiero** que mi sesión se mantenga mientras trabajo y poder cerrarla, **para** no tener que volver a ingresar a cada rato y proteger el equipo si lo pierdo.

## Criterios de aceptación

1. **Dado:** una sesión vigente. **Cuando:** vence el token de acceso. **Entonces:** se renueva en segundo plano sin interrumpirme.
2. **Dado:** un usuario. **Cuando:** elige cerrar sesión. **Entonces:** el token de refresco se invalida y se limpian los datos locales.
3. **Dado:** un técnico en el celular. **Cuando:** cierra sesión. **Entonces:** se borran las órdenes guardadas en el dispositivo (si hay datos offline, avisa antes si hay cambios sin sincronizar).
4. **Dado:** un administrador. **Cuando:** da de baja a un usuario. **Entonces:** sus sesiones activas dejan de funcionar.
