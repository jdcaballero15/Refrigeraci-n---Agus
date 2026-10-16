---
id: E06-06
title: "Registrar la devolución del equipo con firma del cliente"
epic: E06
phase: 1
priority: must
status: draft
roles: [technician]
size: M
areas: [backend, pwa]
depends_on: [E06-05, E05-07]
blocked_by: []
assumes: []
---

# E06-06 Registrar la devolución del equipo con firma del cliente

## Historia

**Como** técnico, **quiero** registrar la devolución del equipo con la firma del cliente, **para** tener constancia de la entrega.

## Criterios de aceptación

1. **Dado:** una etapa de devolución asignada a mí. **Cuando:** la completo con firma, nombre y DNI. **Entonces:** la etapa queda `done`, el equipo sale del galpón y la orden pasa a `Terminada`.
2. **Dado:** una devolución sin firma. **Cuando:** intento completarla. **Entonces:** se rechaza.
3. **Dado:** la devolución completada. **Cuando:** se consulta. **Entonces:** se puede generar el comprobante PDF (E09-02).
