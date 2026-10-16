---
id: E00-10
title: "Envío de mail transaccional"
epic: E00
phase: 1
priority: must
status: draft
roles: [dev]
size: S
areas: [backend, infra]
depends_on: [E00-01]
blocked_by: [D-009]
assumes: []
---

# E00-10 Envío de mail transaccional

## Historia

**Como** equipo de desarrollo, **quiero** una abstracción de envío de mail con Mailpit en local y un proveedor real en la nube, **para** enviar informes y comprobantes sin atarnos a un proveedor.

## Criterios de aceptación

1. **Dado:** el entorno local. **Cuando:** el sistema envía un mail. **Entonces:** se ve en Mailpit.
2. **Dado:** el proveedor real. **Cuando:** se envía un mail desde staging. **Entonces:** llega desde el dominio de la empresa con SPF y DKIM válidos.
3. **Dado:** un envío fallido. **Cuando:** el proveedor responde con error. **Entonces:** se reintenta con espera creciente y queda registrado el estado final.
4. **Dado:** el contenido de un mail. **Cuando:** se registra el envío. **Entonces:** el log no guarda el cuerpo ni adjuntos.
