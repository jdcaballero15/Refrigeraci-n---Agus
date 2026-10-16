---
id: E99-05
title: "Emisión de factura electrónica"
epic: E99
phase: 2
priority: could
status: icebox
roles: [admin]
size: L
areas: [backend]
depends_on: []
blocked_by: []
assumes: []
---

# E99-05 Emisión de factura electrónica

## Historia

**Como** administración, **quiero** emitir la factura electrónica desde el sistema, **para** no cargar los datos dos veces.

## Criterios de aceptación

1. **Dado:** una orden revisada. **Cuando:** administración emite la factura. **Entonces:** se genera la factura electrónica y se registra su número.

## Notas técnicas

- Fuera de alcance. Si el cliente cambia de sistema de facturación, se encara como proyecto aparte.
