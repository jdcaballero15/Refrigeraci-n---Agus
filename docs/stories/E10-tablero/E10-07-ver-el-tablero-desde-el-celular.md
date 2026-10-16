---
id: E10-07
title: "Ver el tablero desde el celular"
epic: E10
phase: 1
priority: must
status: draft
roles: [owner]
size: S
areas: [web-admin]
depends_on: [E10-01]
blocked_by: []
assumes: []
---

# E10-07 Ver el tablero desde el celular

## Historia

**Como** dirección, **quiero** abrir el tablero desde el celular, **para** seguir el negocio sin estar en la oficina.

## Criterios de aceptación

1. **Dado:** el tablero. **Cuando:** lo abro en una pantalla de celular. **Entonces:** se adapta al ancho sin desplazamiento horizontal.
2. **Dado:** dirección. **Cuando:** inicia sesión desde el celular. **Entonces:** ve el tablero como pantalla principal.
3. **Dado:** el tablero. **Cuando:** carga en una conexión móvil común. **Entonces:** es usable en menos de 3 segundos.

## Notas técnicas

- La propuesta original pedía "se puede ver desde el celular". El tablero es parte de `web-admin` responsive.
