---
id: E04-09
title: "Registrar la factura de una orden"
epic: E04
phase: 1
priority: must
status: draft
roles: [admin]
size: S
areas: [backend, web-admin]
depends_on: [E04-08]
blocked_by: []
assumes: [D-004]
---

# E04-09 Registrar la factura de una orden

## Historia

**Como** administración, **quiero** registrar el número de factura de una orden revisada, **para** llevar el control de lo facturado sin duplicar la carga en otro lado.

## Criterios de aceptación

1. **Dado:** una orden `Terminada` y revisada. **Cuando:** administración registra un número de factura. **Entonces:** pasa a `Facturada` y queda un registro de factura con usuario y fecha.
2. **Dado:** una orden sin revisar. **Cuando:** se intenta registrar la factura. **Entonces:** se rechaza.
3. **Dado:** un número de factura vacío. **Cuando:** se intenta guardar. **Entonces:** se rechaza.
4. **Dado:** una orden `Facturada`. **Cuando:** administración corrige el número de factura. **Entonces:** queda auditado el valor anterior y el nuevo.

## Preguntas abiertas

- ¿Una misma factura puede cubrir varias órdenes (por ejemplo, abonados)? De ser así, se agrega la acción en bloque.
- Datos exactos que administración necesita para facturar: ver `D-004`.

## Fuera de alcance

- Emisión de la factura electrónica: se sigue haciendo en el sistema de facturación del cliente.
