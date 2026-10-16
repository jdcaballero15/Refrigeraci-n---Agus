---
id: E05-09
title: "Guardar mis órdenes en el celular para trabajar sin señal"
epic: E05
phase: 1
priority: must
status: draft
roles: [technician]
size: L
areas: [pwa]
depends_on: [E05-01, E00-03]
blocked_by: [D-001]
assumes: []
---

# E05-09 Guardar mis órdenes en el celular para trabajar sin señal

## Historia

**Como** técnico, **quiero** tener mis órdenes guardadas en el celular, **para** poder trabajar en cámaras, sótanos o zonas rurales sin señal.

## Criterios de aceptación

1. **Dado:** un técnico con conexión. **Cuando:** abre la app. **Entonces:** sus órdenes asignadas se guardan en el celular.
2. **Dado:** el celular sin señal. **Cuando:** abre la app. **Entonces:** ve y abre sus órdenes guardadas.
3. **Dado:** lo guardado en el celular. **Cuando:** se inspecciona. **Entonces:** no contiene precios, mano de obra ni historial.
4. **Dado:** un técnico que cierra sesión. **Cuando:** hay datos locales. **Entonces:** se borran tras confirmar que no hay cierres sin sincronizar.

## Notas técnicas

- IndexedDB. Ver ADR 0003. Si `D-001` resuelve que no hace falta offline, esta historia y E05-10 y E05-11 pasan a icebox.
