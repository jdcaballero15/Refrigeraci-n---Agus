---
id: E05-06
title: "Agregar foto y observación al cierre"
epic: E05
phase: 1
priority: must
status: draft
roles: [technician]
size: M
areas: [backend, pwa]
depends_on: [E05-04, E00-09]
blocked_by: []
assumes: []
---

# E05-06 Agregar foto y observación al cierre

## Historia

**Como** técnico, **quiero** adjuntar una foto y escribir una observación al cerrar, **para** dejar evidencia del trabajo y aclaraciones.

## Criterios de aceptación

1. **Dado:** un cierre en curso. **Cuando:** saco o elijo una foto. **Entonces:** se comprime en el celular y se sube al bucket con URL firmada.
2. **Dado:** una foto. **Cuando:** se sube. **Entonces:** la base guarda solo la clave del objeto, tipo y tamaño.
3. **Dado:** una subida que falla. **Cuando:** hay mala señal. **Entonces:** se reintenta sin perder la foto.
4. **Dado:** la observación. **Cuando:** la escribo. **Entonces:** es opcional salvo que haya elegido "Otro" o una medición fuera de rango.

## Preguntas abiertas

- ¿La foto es obligatoria? ¿Una sola o varias? La propuesta dice "una observación y una foto".
