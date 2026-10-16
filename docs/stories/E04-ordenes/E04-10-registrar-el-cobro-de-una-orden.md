---
id: E04-10
title: "Registrar el cobro de una orden"
epic: E04
phase: 1
priority: must
status: draft
roles: [admin]
size: S
areas: [backend, web-admin]
depends_on: [E04-09]
blocked_by: []
assumes: []
---

# E04-10 Registrar el cobro de una orden

## Historia

**Como** administración, **quiero** registrar que una orden facturada fue cobrada, **para** cerrar el circuito y saber qué falta cobrar.

## Criterios de aceptación

1. **Dado:** una orden `Facturada`. **Cuando:** administración registra el cobro. **Entonces:** pasa a `Cobrada` y queda un registro de cobro con usuario y fecha.
2. **Dado:** una orden que no está `Facturada`. **Cuando:** se intenta registrar el cobro. **Entonces:** se rechaza.
3. **Dado:** una orden `Cobrada`. **Cuando:** se consulta. **Entonces:** es de solo lectura.
4. **Dado:** un cobro registrado por error. **Cuando:** administración lo anula. **Entonces:** queda auditado y la orden vuelve a `Facturada`.

## Preguntas abiertas

- ¿Se necesita registrar importe, medio o fecha de pago reales, o alcanza con marcar cobrada?
