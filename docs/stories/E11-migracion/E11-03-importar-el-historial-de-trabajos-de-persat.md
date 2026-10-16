---
id: E11-03
title: "Importar el historial de trabajos de Persat"
epic: E11
phase: 1
priority: must
status: draft
roles: [admin]
size: L
areas: [backend, datos]
depends_on: [E11-02, E04-06]
blocked_by: [D-010]
assumes: []
---

# E11-03 Importar el historial de trabajos de Persat

## Historia

**Como** administración, **quiero** importar el historial de trabajos de Persat, **para** poder mostrar el historial de cada cliente y equipo desde el primer día.

## Criterios de aceptación

1. **Dado:** un archivo de historial. **Cuando:** se importa en modo prueba. **Entonces:** se muestra cuántos trabajos se importarían y a qué clientes y equipos se asocian.
2. **Dado:** un trabajo importado. **Cuando:** se consulta. **Entonces:** figura en el historial del cliente y del equipo marcado como "importado desde Persat".
3. **Dado:** los trabajos importados. **Cuando:** se consultan. **Entonces:** no se mezclan con las estadísticas del sistema nuevo salvo que se pida explícitamente.
4. **Dado:** el historial importado. **Cuando:** se ve. **Entonces:** es de solo lectura.

## Notas técnicas

- Se sumó al alcance: originalmente estaba fuera. El cliente confirmó que Persat es exportable.

## Preguntas abiertas

- Qué campos trae el historial de Persat (fechas, técnico, repuestos, observaciones) define cuánto se puede mapear a falla y reparación.
