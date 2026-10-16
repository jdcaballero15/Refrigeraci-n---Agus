# Definición de Terminado

Una historia está terminada cuando se cumple **todo** lo siguiente.

## Producto

- [ ] Todos los criterios de aceptación de la historia se cumplen.
- [ ] Cada criterio tiene al menos un test automático (o una justificación escrita si no es automatizable).
- [ ] Los textos de la interfaz están en español, claros y sin jerga técnica.
- [ ] Probado en el dispositivo real que corresponde (celular Android para la PWA, tablet o PC para administración).

## Reglas de dominio

- [ ] Ninguna respuesta del rol técnico incluye precios, mano de obra ni historial de clientes. El test de contrato pasa.
- [ ] Cada endpoint declara el rol requerido y tiene test de acceso denegado.
- [ ] No hay `DELETE` físico. Los borrados son lógicos.
- [ ] Fechas de negocio y precios se guardan en tablas de transacción.
- [ ] Los precios de repuestos se estampan al usarlos.
- [ ] Las fotos y firmas van al bucket, no a la base.

## Calidad técnica

- [ ] CI en verde (`ci-ok`).
- [ ] Migraciones con `upgrade` y `downgrade` probados.
- [ ] Sin warnings nuevos de lint ni de tipos.
- [ ] Sin código muerto ni TODO sin historia asociada.
- [ ] Revisión de Claude atendida: cada comentario resuelto o descartado con una línea de justificación.

## Seguridad y datos

- [ ] Sin secretos, tokens ni cadenas de conexión en el código.
- [ ] Sin datos reales (DNI, firmas, clientes, precios) en código, tests, capturas, logs ni issues.
- [ ] Los logs nuevos no incluyen datos personales.

## Documentación

- [ ] La historia pasó a `estado: hecha` y tiene notas técnicas si hubo decisiones.
- [ ] Se actualizó el ADR, el modelo de datos o el glosario si cambió algo de eso.
- [ ] Si se resolvió una decisión pendiente, se actualizó `docs/domain/decisiones-pendientes.md` y se quitó `blocked_by` de las historias.
