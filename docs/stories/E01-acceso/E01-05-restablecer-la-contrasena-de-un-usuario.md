---
id: E01-05
title: "Restablecer la contraseña de un usuario"
epic: E01
phase: 1
priority: should
status: draft
roles: [admin]
size: S
areas: [backend, web-admin]
depends_on: [E01-03]
blocked_by: []
assumes: []
---

# E01-05 Restablecer la contraseña de un usuario

## Historia

**Como** administración, **quiero** restablecer la contraseña de un usuario que la olvidó, **para** que un técnico no quede sin trabajar por un olvido.

## Criterios de aceptación

1. **Dado:** administración. **Cuando:** restablece la contraseña de un usuario. **Entonces:** se genera una contraseña temporal que se muestra una sola vez.
2. **Dado:** un usuario con contraseña temporal. **Cuando:** inicia sesión. **Entonces:** debe cambiarla antes de seguir.
3. **Dado:** un restablecimiento. **Cuando:** se realiza. **Entonces:** queda en la auditoría con quién lo hizo y sobre quién.
4. **Dado:** un técnico. **Cuando:** intenta restablecer una contraseña. **Entonces:** recibe acceso denegado.

## Preguntas abiertas

- ¿Hace falta que cada usuario pueda recuperar su contraseña por correo por su cuenta?
