---
id: E11-01
title: "Importar clientes desde Persat"
epic: E11
phase: 1
priority: must
status: draft
roles: [admin]
size: M
areas: [backend, datos]
depends_on: [E03-01, E11-05]
blocked_by: [D-010]
assumes: []
---

# E11-01 Importar clientes desde Persat

## Historia

**Como** administración, **quiero** importar los clientes desde la exportación de Persat, **para** no cargar a mano 50 a 200 clientes.

## Criterios de aceptación

1. **Dado:** un archivo de exportación válido. **Cuando:** se importa en modo prueba. **Entonces:** se muestra cuántos clientes se crearían, cuáles ya existen y cuáles tienen errores, sin guardar nada.
2. **Dado:** la confirmación. **Cuando:** se aplica. **Entonces:** se crean los clientes y cada uno guarda su referencia al identificador de Persat.
3. **Dado:** una segunda importación del mismo archivo. **Cuando:** se ejecuta. **Entonces:** no crea duplicados.
4. **Dado:** una fila con datos inválidos. **Cuando:** se importa. **Entonces:** se informa con su número y el motivo.
