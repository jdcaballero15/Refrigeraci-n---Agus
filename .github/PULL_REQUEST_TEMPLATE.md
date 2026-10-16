## Historia

Cierra #<!-- número de issue --> · ID: `E00-00`

## Qué cambia

<!-- Resumen en 2 o 3 líneas. Qué y por qué, no cómo. -->

## Cómo se probó

<!-- Tests automáticos agregados y pasos manuales si corresponde. -->

## Checklist (Definición de Terminado)

- [ ] Cumple todos los criterios de aceptación de la historia
- [ ] Cada criterio tiene al menos un test
- [ ] Las respuestas para el rol técnico no incluyen precios, mano de obra ni historial (si aplica)
- [ ] Borrado lógico, sin `DELETE` físico (si aplica)
- [ ] Migración reversible y probada hacia arriba y hacia abajo (si aplica)
- [ ] Sin secretos, DNI, firmas ni datos reales en código, tests, capturas o logs
- [ ] Documentación e historia actualizadas (estado, notas técnicas)
- [ ] Título del PR en formato Conventional Commits
- [ ] `make lint` y `make test` en verde en mi máquina
- [ ] Ninguna regla apagada para que pase el CI (`# noqa` genérico, `--no-verify`, excluir archivos)
- [ ] Si hubo una decisión de arquitectura, escribí el ADR en `docs/architecture/adr/`
- [ ] Si agregué una variable de entorno, actualicé `.env.example` (valor vacío)
- [ ] Dinero con `Decimal`, llamadas externas con timeout y reintento, escrituras con idempotencia (si aplica)

## Notas para quien revisa

<!-- Riesgos, decisiones, cosas que quedan fuera. Capturas si hay cambios de interfaz (sin datos reales). -->
