---
id: E09-01
title: "Generar el comprobante PDF de retiro"
epic: E09
phase: 1
priority: must
status: draft
roles: [admin]
size: M
areas: [backend, web-admin]
depends_on: [E06-04, E00-09]
blocked_by: []
assumes: []
---

# E09-01 Generar el comprobante PDF de retiro

## Historia

**Como** administración, **quiero** generar un PDF del retiro de un equipo con la firma del cliente, **para** enviarle al cliente constancia de lo que se llevó.

## Criterios de aceptación

1. **Dado:** una etapa de retiro completada. **Cuando:** administración genera el comprobante. **Entonces:** se crea un PDF con cliente, equipo, fecha, técnico, estado declarado, nombre y DNI de quien firmó y la imagen de la firma.
2. **Dado:** el PDF. **Cuando:** se genera. **Entonces:** no incluye precios.
3. **Dado:** un comprobante generado. **Cuando:** se vuelve a pedir. **Entonces:** se devuelve el mismo archivo almacenado.
4. **Dado:** una etapa de retiro sin completar. **Cuando:** se pide el comprobante. **Entonces:** se rechaza.

## Notas técnicas

- El PDF se guarda en el bucket. El DNI y la firma son datos personales: ver `SECURITY.md`.
