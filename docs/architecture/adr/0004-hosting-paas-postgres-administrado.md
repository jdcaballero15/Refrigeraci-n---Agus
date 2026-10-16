# ADR 0004: Hosting en PaaS con PostgreSQL administrado

**Estado:** Aceptado. El proveedor concreto se elige en la historia E00-05.

## Contexto

La carga es mínima, pero perder órdenes o cobros es el peor escenario, y el sistema maneja datos personales (nombre, DNI y firma de clientes). Quien lo mantiene es una consultora chica. La propuesta al cliente dice que el sistema "es de ustedes, sin abono obligatorio".

## Decisión

- Contenedores Docker desplegados en un **PaaS** (Railway, Render o Fly.io).
- **PostgreSQL administrado**, con backups automáticos y restauración a un punto en el tiempo.
- **Bucket S3 compatible** (Cloudflare R2, Backblaze B2 o S3) para fotos, firmas y PDF.
- Las **cuentas de hosting, base y bucket se crean a nombre del cliente**, con MendoData como administrador.
- Dos entornos: staging (automático desde `main`) y producción (tag con aprobación).

## Criterios para elegir proveedor (E00-05)

1. Backups con restauración a un punto en el tiempo incluidos.
2. Región cercana (Sudamérica) si existe, por latencia.
3. Costo mensual en dólares estable y predecible. Se informa al cliente como referencia con cotización y fecha.
4. Cron jobs o scheduler nativo para los jobs mensuales.
5. Facilidad para migrar a otro proveedor o a un VPS (solo Docker y variables de entorno).

## Alternativas descartadas

- **VPS único con Docker Compose**: el más barato, pero MendoData pasa a ser sysadmin del cliente (backups, parches, caídas).
- **AWS (ECS, RDS, S3)**: sobredimensionado para este volumen.

## Consecuencias

- El costo mensual es mayor que un VPS, a cambio de menos riesgo operativo.
- Al ser portable, si el costo molesta se mueve a un VPS sin reescribir.
- Hay un costo recurrente en dólares que no existía con Microsoft 365. Se tiene que hablar con el cliente antes de contratar (`D-006`).
