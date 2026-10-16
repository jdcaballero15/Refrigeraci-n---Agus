---
id: E05-10
title: "Cola de cierres pendientes de sincronizar"
epic: E05
phase: 1
priority: must
status: draft
roles: [technician]
size: L
areas: [pwa]
depends_on: [E05-09, E05-12]
blocked_by: [D-001]
assumes: []
---

# E05-10 Cola de cierres pendientes de sincronizar

## Historia

**Como** técnico, **quiero** que mis cierres, firmas y fotos queden en una cola y se envíen solos cuando vuelva la señal, **para** no perder trabajo hecho sin conexión.

## Criterios de aceptación

1. **Dado:** un cierre completado sin señal. **Cuando:** toco "Enviar". **Entonces:** queda guardado en la cola local con una clave de idempotencia.
2. **Dado:** la señal que vuelve. **Cuando:** la app lo detecta. **Entonces:** envía la cola en orden sin acción del técnico.
3. **Dado:** un envío reintentado por corte de red. **Cuando:** el servidor ya lo había recibido. **Entonces:** no se duplica el cierre.
4. **Dado:** una foto o firma. **Cuando:** se sube con mala señal. **Entonces:** se reintenta hasta lograrlo.
5. **Dado:** el técnico que cierra la app o apaga el celular. **Cuando:** lo vuelve a abrir. **Entonces:** la cola sigue intacta.
