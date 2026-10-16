---
id: E01-04
title: "Autorización por rol en la API"
epic: E01
phase: 1
priority: must
status: draft
roles: [admin, technician, owner]
size: M
areas: [backend]
depends_on: [E01-01, E00-04]
blocked_by: []
assumes: []
---

# E01-04 Autorización por rol en la API

## Historia

**Como** dirección, **quiero** que cada rol solo pueda hacer y ver lo permitido por la matriz de permisos, **para** proteger la información sensible aunque alguien manipule la aplicación.

## Criterios de aceptación

1. **Dado:** una ruta de la API. **Cuando:** se declara. **Entonces:** exige explícitamente uno o más roles mediante una dependencia común.
2. **Dado:** un técnico. **Cuando:** pide una orden que no tiene asignada, por su ID. **Entonces:** recibe 404 (no 403, para no confirmar que existe).
3. **Dado:** un técnico. **Cuando:** llama a una ruta de administración. **Entonces:** recibe 403.
4. **Dado:** la matriz de `docs/domain/roles-permisos.md`. **Cuando:** se ejecutan los tests. **Entonces:** hay un test de acceso permitido y uno denegado por cada ruta.
5. **Dado:** una ruta nueva sin rol declarado. **Cuando:** corre CI. **Entonces:** el test de rutas falla.

## Notas técnicas

- Rutas del técnico bajo `/tech/`, de administración bajo `/admin/`. Ver ADR 0006.
