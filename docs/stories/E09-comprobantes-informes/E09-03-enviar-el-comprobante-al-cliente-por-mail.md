---
id: E09-03
title: "Enviar el comprobante al cliente por mail"
epic: E09
phase: 1
priority: must
status: draft
roles: [admin]
size: S
areas: [backend, web-admin]
depends_on: [E09-01, E00-10]
blocked_by: []
assumes: []
---

# E09-03 Enviar el comprobante al cliente por mail

## Historia

**Como** administración, **quiero** enviar el comprobante de retiro o devolución por mail al cliente, **para** darle la constancia sin salir del sistema.

## Criterios de aceptación

1. **Dado:** un comprobante generado. **Cuando:** administración elige un contacto del cliente y envía. **Entonces:** el mail llega con el PDF adjunto y queda registrado quién lo envió y cuándo.
2. **Dado:** un envío fallido. **Cuando:** el proveedor devuelve error. **Entonces:** administración ve el estado y puede reenviar.
3. **Dado:** un cliente sin correo cargado. **Cuando:** se intenta enviar. **Entonces:** se pide cargar un contacto.

## Preguntas abiertas

- La propuesta dice "comprobante en PDF de retiro y de devolución, con la firma, para enviar al cliente". ¿El envío es manual (administración) o automático al completar la etapa?
