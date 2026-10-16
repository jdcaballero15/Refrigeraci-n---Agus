---
id: E01-01
title: "Iniciar sesión con correo y contraseña"
epic: E01
phase: 1
priority: must
status: draft
roles: [admin, technician, owner]
size: S
areas: [backend, web-admin, pwa]
depends_on: [E00-01]
blocked_by: []
assumes: [D-007]
---

# E01-01 Iniciar sesión con correo y contraseña

## Historia

**Como** usuario del sistema, **quiero** iniciar sesión con mi correo y contraseña, **para** acceder solo a lo que corresponde a mi rol.

## Criterios de aceptación

1. **Dado:** un usuario activo con credenciales correctas. **Cuando:** inicia sesión. **Entonces:** recibe una sesión y ve la pantalla de inicio de su rol.
2. **Dado:** credenciales incorrectas. **Cuando:** intenta iniciar sesión. **Entonces:** ve un mensaje genérico que no revela si el correo existe.
3. **Dado:** un usuario dado de baja. **Cuando:** intenta iniciar sesión. **Entonces:** se le rechaza.
4. **Dado:** una contraseña. **Cuando:** se guarda. **Entonces:** se almacena con Argon2 y nunca en texto plano ni en logs.

## Notas técnicas

- Sesión con JWT de corta duración y token de refresco rotativo. Ver E01-02.
