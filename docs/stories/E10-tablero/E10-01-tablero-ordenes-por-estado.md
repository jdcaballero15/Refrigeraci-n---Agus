---
id: E10-01
title: "Tablero: órdenes por estado"
epic: E10
phase: 1
priority: must
status: draft
roles: [owner, admin]
size: M
areas: [backend, web-admin]
depends_on: [E04-05]
blocked_by: []
assumes: []
---

# E10-01 Tablero: órdenes por estado

## Historia

**Como** dirección, **quiero** ver cuántas órdenes hay en cada estado y cómo evolucionan, **para** saber cómo va el trabajo de un vistazo.

## Criterios de aceptación

1. **Dado:** órdenes en varios estados. **Cuando:** abro el tablero. **Entonces:** veo la cantidad por estado y una evolución por semana o mes.
2. **Dado:** el tablero. **Cuando:** selecciono un estado. **Entonces:** llego a la lista de esas órdenes.
3. **Dado:** los datos. **Cuando:** se calculan. **Entonces:** coinciden con el panel de órdenes (E04-05).

## Notas técnicas

- Reemplaza a la opción "tablero en Power BI" de la propuesta original. Si más adelante se quiere Power BI, se expone una vista de datos de solo lectura.
