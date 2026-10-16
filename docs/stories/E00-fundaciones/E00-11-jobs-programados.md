---
id: E00-11
title: "Jobs programados"
epic: E00
phase: 1
priority: must
status: draft
roles: [dev]
size: S
areas: [backend, infra]
depends_on: [E00-01]
blocked_by: []
assumes: []
---

# E00-11 Jobs programados

## Historia

**Como** equipo de desarrollo, **quiero** un mecanismo de tareas programadas confiable, **para** ejecutar la generación mensual de mantenimiento y el informe mensual sin intervención.

## Criterios de aceptación

1. **Dado:** un job programado. **Cuando:** llega su horario. **Entonces:** se ejecuta una sola vez aunque haya más de una instancia del backend.
2. **Dado:** un job que falla. **Cuando:** termina con error. **Entonces:** queda registrado y se reintenta sin duplicar su efecto.
3. **Dado:** un administrador de sistema. **Cuando:** quiere ejecutar un job a mano. **Entonces:** puede hacerlo con un comando seguro para repetir (idempotente).
4. **Dado:** los horarios. **Cuando:** se configuran. **Entonces:** usan la zona horaria America/Argentina/Mendoza.

## Notas técnicas

- Opciones: scheduler del PaaS invocando un endpoint interno protegido, o un proceso aparte con bloqueo en Postgres (advisory lock).
