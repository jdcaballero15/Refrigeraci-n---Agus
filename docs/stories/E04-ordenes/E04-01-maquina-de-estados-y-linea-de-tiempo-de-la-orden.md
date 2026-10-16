---
id: E04-01
title: "Máquina de estados y línea de tiempo de la orden"
epic: E04
phase: 1
priority: must
status: draft
roles: [admin]
size: M
areas: [backend]
depends_on: [E00-01]
blocked_by: []
assumes: []
---

# E04-01 Máquina de estados y línea de tiempo de la orden

## Historia

**Como** administración, **quiero** que las órdenes solo puedan pasar por transiciones de estado válidas y que cada cambio quede registrado, **para** no perder ninguna orden en el traspaso entre oficina y campo y poder reconstruir qué pasó.

## Criterios de aceptación

1. **Dado:** una orden en cualquier estado. **Cuando:** se intenta una transición no permitida por `order-state-machine.md`. **Entonces:** se rechaza con un mensaje claro y no se modifica nada.
2. **Dado:** una transición válida. **Cuando:** se aplica. **Entonces:** se inserta un evento con estado anterior, estado nuevo, usuario y fecha en la misma transacción que actualiza `work_order.status`.
3. **Dado:** dos usuarios. **Cuando:** intentan cambiar el estado de la misma orden a la vez. **Entonces:** solo uno lo logra y el otro recibe un error de conflicto.
4. **Dado:** una orden en `Cobrada` o `Cancelada`. **Cuando:** se intenta cambiar su estado. **Entonces:** se rechaza.
5. **Dado:** la tabla de transiciones. **Cuando:** corren los tests. **Entonces:** hay un test por cada transición permitida y por cada categoría de transición prohibida.

## Notas técnicas

- Lógica pura en `app/domain/`, sin SQLAlchemy. Fechas de negocio salen de `work_order_event` (ADR 0005).
- Agregar `event_type` a `work_order_event` para registrar eventos que no cambian el estado (revisión, asignación).
- Los 7 estados: Pendiente, Asignada, En curso, Terminada, Facturada, Cobrada, Cancelada.

## Preguntas abiertas

- Validar con negocio la tabla de transiciones propuesta, en particular cancelar solo antes de Terminada y devolver al técnico una orden Terminada.
