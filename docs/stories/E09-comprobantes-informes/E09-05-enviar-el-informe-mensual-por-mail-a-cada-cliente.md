---
id: E09-05
title: "Enviar el informe mensual por mail a cada cliente"
epic: E09
phase: 1
priority: must
status: draft
roles: [admin]
size: M
areas: [backend]
depends_on: [E09-04, E00-10, E00-11, E03-01]
blocked_by: []
assumes: []
---

# E09-05 Enviar el informe mensual por mail a cada cliente

## Historia

**Como** administración, **quiero** que el informe mensual llegue por mail a los contactos de cada cliente, **para** mantener informados a los clientes sin trabajo manual.

## Criterios de aceptación

1. **Dado:** el día configurado del mes. **Cuando:** corre el job. **Entonces:** envía el informe del mes anterior a los contactos marcados de cada cliente.
2. **Dado:** el job. **Cuando:** se ejecuta dos veces para el mismo período. **Entonces:** no envía el mismo informe dos veces.
3. **Dado:** un envío. **Cuando:** falla. **Entonces:** se reintenta y queda el estado en la entrega.
4. **Dado:** un cliente sin contactos marcados. **Cuando:** corre el job. **Entonces:** se omite y aparece en el resumen de la corrida.
