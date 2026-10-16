---
id: E11-09
title: "Datos de prueba ficticios"
epic: E11
phase: 1
priority: must
status: ready
roles: [dev]
size: S
areas: [backend, datos]
depends_on: [E00-01]
blocked_by: []
assumes: []
---

# E11-09 Datos de prueba ficticios

## Historia

**Como** equipo de desarrollo, **quiero** un generador de datos de prueba ficticios (clientes, equipos, órdenes, stock), **para** desarrollar, probar y capacitar sin usar datos reales.

## Criterios de aceptación

1. **Dado:** una base vacía. **Cuando:** corro el generador. **Entonces:** crea clientes, equipos, técnicos, órdenes en todos los estados, repuestos y movimientos de stock ficticios.
2. **Dado:** los datos generados. **Cuando:** se revisan. **Entonces:** no contienen DNI, nombres ni direcciones reales.
3. **Dado:** el generador. **Cuando:** se ejecuta dos veces. **Entonces:** es repetible con una semilla fija.
