---
id: E03-02
title: "Domicilios o sitios de un cliente"
epic: E03
phase: 1
priority: must
status: draft
roles: [admin]
size: S
areas: [backend, web-admin]
depends_on: [E03-01]
blocked_by: []
assumes: []
---

# E03-02 Domicilios o sitios de un cliente

## Historia

**Como** administración, **quiero** registrar uno o más domicilios o sucursales por cliente, **para** saber a dónde ir y dónde está cada equipo.

## Criterios de aceptación

1. **Dado:** un cliente. **Cuando:** administración le agrega un domicilio con etiqueta y dirección. **Entonces:** el domicilio se ofrece al crear órdenes de ese cliente.
2. **Dado:** un domicilio con equipos. **Cuando:** se quiere eliminar. **Entonces:** solo se puede desactivar.
3. **Dado:** el técnico con una orden asignada. **Cuando:** la abre. **Entonces:** ve la dirección del domicilio de esa orden y nada de otros domicilios del cliente.
