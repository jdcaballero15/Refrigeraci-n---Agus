---
id: E00-05
title: "Elegir proveedor de hosting y desplegar staging"
epic: E00
phase: 1
priority: must
status: draft
roles: [dev]
size: M
areas: [infra]
depends_on: [E00-01]
blocked_by: [D-006]
assumes: []
---

# E00-05 Elegir proveedor de hosting y desplegar staging

## Historia

**Como** equipo de desarrollo, **quiero** elegir el proveedor de hosting con los criterios del ADR 0004 y desplegar un entorno de staging, **para** tener un entorno real donde probar cada cambio.

## Criterios de aceptación

1. **Dado:** los criterios del ADR 0004. **Cuando:** se comparan al menos dos proveedores. **Entonces:** queda documentada la elección y el costo mensual estimado con fecha de cotización.
2. **Dado:** un merge a `main`. **Cuando:** termina CI. **Entonces:** staging se despliega solo y `GET /health` responde ok.
3. **Dado:** staging. **Cuando:** se revisan las cuentas. **Entonces:** el hosting, la base y el bucket están a nombre de la empresa cliente (o con un plan de traspaso documentado).
4. **Dado:** el despliegue. **Cuando:** se revisan variables. **Entonces:** ninguna credencial está en el repositorio.

## Notas técnicas

- Actualizar ADR 0004 con el proveedor elegido. El costo recurrente se gestiona fuera del repo.
