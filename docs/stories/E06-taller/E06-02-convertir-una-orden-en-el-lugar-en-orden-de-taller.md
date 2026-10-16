---
id: E06-02
title: "Convertir una orden en el lugar en orden de taller"
epic: E06
phase: 1
priority: must
status: draft
roles: [technician, admin]
size: M
areas: [backend, pwa]
depends_on: [E05-08, E06-01]
blocked_by: []
assumes: []
---

# E06-02 Convertir una orden en el lugar en orden de taller

## Historia

**Como** técnico, **quiero** marcar "requiere retiro" al cerrar una orden en el lugar, **para** que la misma orden siga en taller sin perder lo ya registrado.

## Criterios de aceptación

1. **Dado:** una orden en el lugar `En curso`. **Cuando:** el técnico elige "requiere retiro". **Entonces:** la orden pasa a tipo taller, conserva lo registrado y se crean las etapas.
2. **Dado:** la conversión. **Cuando:** ocurre. **Entonces:** la etapa de retiro queda disponible para asignar y administración recibe el aviso.
3. **Dado:** una orden convertida. **Cuando:** se consulta. **Entonces:** sigue siendo la misma orden, mismo número e historial.
4. **Dado:** la conversión. **Cuando:** se realiza. **Entonces:** queda un evento con usuario y fecha.
