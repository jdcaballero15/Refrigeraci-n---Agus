---
id: E01-06
title: "Bloqueo temporal por intentos fallidos"
epic: E01
phase: 1
priority: should
status: draft
roles: [admin, technician, owner]
size: S
areas: [backend]
depends_on: [E01-01]
blocked_by: []
assumes: []
---

# E01-06 Bloqueo temporal por intentos fallidos

## Historia

**Como** dirección, **quiero** que el sistema frene los intentos repetidos de adivinar contraseñas, **para** proteger las cuentas.

## Criterios de aceptación

1. **Dado:** un usuario. **Cuando:** falla 5 veces seguidas en 10 minutos. **Entonces:** se bloquea el inicio de sesión de esa cuenta durante 15 minutos.
2. **Dado:** un bloqueo. **Cuando:** ocurre. **Entonces:** el usuario ve un mensaje claro con el tiempo de espera y queda registrado.
3. **Dado:** un bloqueo activo. **Cuando:** administración lo revisa. **Entonces:** puede levantarlo manualmente.

## Notas técnicas

- Umbrales configurables. Aplicar también un límite por dirección IP.
