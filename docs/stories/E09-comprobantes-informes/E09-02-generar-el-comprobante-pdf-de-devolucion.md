---
id: E09-02
title: "Generar el comprobante PDF de devolución"
epic: E09
phase: 1
priority: must
status: draft
roles: [admin]
size: S
areas: [backend, web-admin]
depends_on: [E06-06, E09-01]
blocked_by: []
assumes: []
---

# E09-02 Generar el comprobante PDF de devolución

## Historia

**Como** administración, **quiero** generar un PDF de la devolución de un equipo con la firma del cliente, **para** enviarle al cliente constancia de lo recibido.

## Criterios de aceptación

1. **Dado:** una etapa de devolución completada. **Cuando:** administración genera el comprobante. **Entonces:** se crea un PDF con cliente, equipo, fecha, trabajo realizado, nombre y DNI de quien firmó y la firma.
2. **Dado:** el PDF. **Cuando:** se genera. **Entonces:** no incluye precios salvo que negocio indique lo contrario.
3. **Dado:** una etapa sin completar. **Cuando:** se pide el comprobante. **Entonces:** se rechaza.

## Preguntas abiertas

- ¿La devolución debe incluir el resumen del trabajo hecho y los repuestos usados? ¿Con o sin precios?
