# Seguridad

## Este repositorio es público

Nunca se suben al repositorio, ni en commits, issues, PR, capturas ni logs:

- Datos reales de clientes, equipos o trabajos (incluye exportaciones de Persat).
- DNI, firmas, fotos de trabajos o cualquier dato personal real.
- Precios, tarifas, presupuestos o acuerdos comerciales.
- Credenciales, tokens, claves de API, cadenas de conexión (`.env` está en `.gitignore`).

Para desarrollo y tests se usan datos ficticios. Los generadores de datos de prueba viven en `backend/tests/` y `scripts/`.

## Datos personales

El sistema guarda nombre y DNI de quien firma, y firmas manuscritas. Son datos personales (Ley 25.326 de Protección de los Datos Personales, Argentina). Reglas mínimas:

- Cifrado en tránsito (HTTPS) y en reposo (base y bucket gestionados).
- Los archivos (fotos y firmas) se sirven con URLs firmadas de corta duración, nunca públicas.
- Los logs no incluyen DNI, firmas ni contenido de formularios.
- Backups con restauración a un punto en el tiempo, probados.
- Las cuentas de hosting, base y bucket quedan a nombre del cliente.

La política de retención y el texto legal quedan pendientes (ver `D-008` en [docs/domain/decisiones-pendientes.md](docs/domain/decisiones-pendientes.md)).

## Automatizaciones con IA en un repositorio público

- Los workflows de Claude solo corren para colaboradores con permiso de escritura y nunca sobre PR de forks.
- No se usa `pull_request_target` con código del PR.
- Las claves de la API viven en *Secrets* del repositorio, nunca en archivos.
- Los agentes tienen permisos mínimos (ver `.claude/settings.json` y los `permissions:` de cada workflow).

## Reportar una vulnerabilidad

Usar *Security > Report a vulnerability* en GitHub (reporte privado). No abrir un issue público.
