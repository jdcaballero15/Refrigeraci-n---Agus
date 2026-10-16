---
id: E01-03
title: "Gestionar usuarios"
epic: E01
phase: 1
priority: must
status: draft
roles: [admin, owner]
size: M
areas: [backend, web-admin]
depends_on: [E01-04]
blocked_by: []
assumes: []
---

# E01-03 Gestionar usuarios

## Historia

**Como** administración, **quiero** crear, editar y dar de baja usuarios y asignarles un rol, **para** controlar quién usa el sistema.

## Criterios de aceptación

1. **Dado:** administración. **Cuando:** crea un usuario con nombre, correo y rol. **Entonces:** el usuario puede iniciar sesión con una contraseña inicial.
2. **Dado:** un correo ya registrado. **Cuando:** intento crear otro usuario con el mismo. **Entonces:** se rechaza con un mensaje claro.
3. **Dado:** un usuario. **Cuando:** se lo da de baja. **Entonces:** queda inactivo (borrado lógico), conserva su historial y no puede iniciar sesión.
4. **Dado:** un técnico con órdenes asignadas abiertas. **Cuando:** se lo da de baja. **Entonces:** el sistema avisa y pide reasignarlas.
5. **Dado:** un usuario con rol técnico. **Cuando:** intenta acceder a esta pantalla o a su API. **Entonces:** recibe acceso denegado.

## Preguntas abiertas

- ¿Pueden las dos personas de administración gestionar usuarios, o solo dirección?
