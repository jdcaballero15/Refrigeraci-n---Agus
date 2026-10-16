# ADR 0006: Visibilidad por rol resuelta en la API

**Estado:** Aceptado

## Contexto

Requisito del cliente: el técnico nunca ve precios, mano de obra ni historial de clientes. En Power Apps esto se resolvía ocultando controles, lo que no es seguridad real, porque los datos igual llegaban al dispositivo.

## Decisión

- La API devuelve **esquemas distintos por rol**. Para el técnico existe `*TechnicianOut`, que no tiene los campos prohibidos. No es el mismo esquema con campos en `null`.
- Endpoints separados para el técnico (`/tech/...`) y para administración (`/admin/...`). Cada ruta declara el rol requerido por dependencia.
- Un técnico solo accede a las órdenes que tiene asignadas.
- Test de contrato obligatorio: recorre los esquemas del técnico y falla si aparece un campo de precio, mano de obra o historial. Se corre en CI.
- Los logs y respuestas de error no filtran datos prohibidos.
- Lo que la PWA cachea en el celular es lo que la API le entregó, por lo que nunca contiene precios.

## Consecuencias

- Hay más esquemas que mantener, a cambio de seguridad verificable.
- Cualquier campo nuevo en un recurso obliga a decidir en qué esquemas aparece.
- Los revisores (humanos y Claude) tienen una regla concreta para vigilar en cada PR.
