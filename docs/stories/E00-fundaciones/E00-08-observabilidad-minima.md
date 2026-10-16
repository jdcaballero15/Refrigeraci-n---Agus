---
id: E00-08
title: "Observabilidad mínima"
epic: E00
phase: 1
priority: should
status: draft
roles: [dev]
size: S
areas: [backend, infra]
depends_on: [E00-05]
blocked_by: []
assumes: []
---

# E00-08 Observabilidad mínima

## Historia

**Como** equipo de desarrollo, **quiero** logs estructurados sin datos personales, reporte de errores y alerta de caída, **para** enterarnos de un problema antes que el cliente.

## Criterios de aceptación

1. **Dado:** una petición a la API. **Cuando:** se registra el log. **Entonces:** incluye id de petición, ruta, código y duración, y no incluye DNI, firmas, tokens ni cuerpos de formularios.
2. **Dado:** una excepción no controlada. **Cuando:** ocurre. **Entonces:** se reporta al servicio de errores con el id de petición.
3. **Dado:** el chequeo de salud. **Cuando:** falla durante más de 5 minutos. **Entonces:** se envía una alerta a quien mantiene el sistema.
4. **Dado:** un test. **Cuando:** loguea un objeto con campo `dni`. **Entonces:** el valor aparece enmascarado.
