---
id: E08-03
title: "Transferir repuestos entre ubicaciones"
epic: E08
phase: 1
priority: must
status: draft
roles: [admin]
size: S
areas: [backend, web-admin]
depends_on: [E08-02]
blocked_by: []
assumes: []
---

# E08-03 Transferir repuestos entre ubicaciones

## Historia

**Como** administración, **quiero** transferir repuestos del depósito a una camioneta, o entre ubicaciones, **para** que cada técnico salga con lo que necesita.

## Criterios de aceptación

1. **Dado:** una transferencia con origen, destino, repuesto y cantidad. **Cuando:** se registra. **Entonces:** se resta de origen y se suma en destino en una sola transacción.
2. **Dado:** una cantidad mayor al stock del origen. **Cuando:** se intenta transferir. **Entonces:** se rechaza.
3. **Dado:** origen y destino iguales. **Cuando:** se intenta. **Entonces:** se rechaza.
