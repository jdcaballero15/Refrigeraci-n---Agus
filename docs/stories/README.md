# Historias de usuario

Fuente de verdad de lo que el sistema tiene que hacer. Un archivo `.md` por historia, en la carpeta de su épica. Los issues de GitHub se generan desde acá (ver más abajo).

- Índice completo: [INDEX.md](INDEX.md) (se regenera con `python3 scripts/validate_stories.py --write-index`)
- Plantilla: [_template.md](_template.md)
- Decisiones pendientes que bloquean historias: [../domain/decisiones-pendientes.md](../domain/decisiones-pendientes.md)

## Épicas

| Épica | Tema |
|---|---|
| [E00](E00-fundaciones/README.md) | Fundaciones de plataforma |
| [E01](E01-acceso/README.md) | Acceso, usuarios y roles |
| [E02](E02-catalogos/README.md) | Catálogos |
| [E03](E03-clientes-equipos/README.md) | Clientes y equipos |
| [E04](E04-ordenes/README.md) | Órdenes de trabajo (administración) |
| [E05](E05-app-tecnico/README.md) | App del técnico |
| [E06](E06-taller/README.md) | Órdenes de taller |
| [E07](E07-mantenimiento/README.md) | Mantenimiento preventivo |
| [E08](E08-stock/README.md) | Stock de repuestos |
| [E09](E09-comprobantes-informes/README.md) | Comprobantes e informes |
| [E10](E10-tablero/README.md) | Tablero de seguimiento |
| [E11](E11-migracion/README.md) | Migración y puesta en marcha |
| [E12](E12-transversal/README.md) | Transversal: auditoría, privacidad y calidad |
| [E99](E99-icebox/README.md) | Icebox: fuera de alcance por ahora |

## Formato de una historia

Archivo `docs/stories/<EXX-epica>/EXX-NN-titulo-corto.md` con encabezado YAML:

```yaml
---
id: E04-03
title: Asignar una orden a un técnico
epic: E04
phase: 1                 # 1 o 2
priority: must           # must (debe), should (debería), could (podría)
status: draft            # draft, ready, in_progress, done, icebox
roles: [admin]           # admin, technician, owner, dev
size: S                  # XS, S, M, L (L conviene dividirla)
areas: [backend, web-admin]   # backend, web-admin, pwa, infra, datos
depends_on: [E04-02]     # historias que tienen que existir antes
blocked_by: []           # decisiones ABIERTAS (D-0XX) que impiden implementarla
assumes: []              # decisiones con PROPUESTA vigente en las que se apoya
---
```

Cuerpo: **Historia** (Como, quiero, para), **Criterios de aceptación** (Dado: contexto. Cuando: acción. Entonces: resultado), y opcionalmente **Notas técnicas**, **Preguntas abiertas** y **Fuera de alcance**.

## Estados

| Estado | Significado | ¿Se puede implementar? |
|---|---|---|
| `draft` | Redactada, sin validar por negocio | No |
| `ready` | Validada: criterios claros, sin bloqueos | **Sí** |
| `in_progress` | En desarrollo (rama abierta) | En curso |
| `done` | Cumple la Definición de Terminado y está en `main` | Terminada |
| `icebox` | Fuera de alcance por ahora | No |

**Una historia con `blocked_by` no puede estar en `ready`.** El validador lo comprueba. Las historias con `assumes` sí pueden implementarse, sabiendo que si la propuesta cambia se vuelve a tocar.

## Prioridad (MoSCoW)

- `must`: sin esto el sistema no cumple el objetivo de la Fase 1.
- `should`: importante, pero hay forma de seguir sin ella.
- `could`: deseable si hay tiempo.

## Ciclo de vida

1. **Redactar** (`/new-story`): queda en `draft`.
2. **Validar**: el analista de negocio revisa los criterios y responde las preguntas abiertas. Se pasa a `ready` en un PR que solo toca la historia.
3. **Implementar** (`/implement-story`): rama `feat/EXX-NN-...`. El PR cambia el estado a `in_progress` al abrirse y a `done` al mergearse.
4. **Si cambia el alcance**: se edita la historia en un PR propio, no a escondidas dentro de un PR de código.

## Issues de GitHub

`.github/workflows/stories-sync.yml` crea o actualiza un issue por historia al mergear a `main`. El título es `[E04-03] Asignar una orden a un técnico` y las etiquetas salen del encabezado (`epica:`, `prioridad:`, `estado:`, `fase:`, `area:`, `bloqueada`). Nunca cierra ni borra issues. Para probarlo sin tocar nada: `make stories-sync-dry`.

## Cómo redactar bien

- **Chica**: entra en un PR de menos de unas 400 líneas. Si no, dividirla.
- **Verificable**: cada criterio se puede convertir en un test. Evitar "rápido" o "fácil" sin un número.
- **Con el caso de error**: qué pasa si falta un dato o no se tiene permiso.
- **Con el técnico a salvo**: si el técnico participa, hay un criterio que dice que no ve precios, mano de obra ni historial.
- **Sin inventar**: lo que no está en el relevamiento va en "Preguntas abiertas".

## Fuera de alcance (confirmado)

- **Registro de hora de llegada y salida del técnico.** El cliente confirmó que no se registra. No hay historia, y no se agrega.

El resto de lo que quedó fuera por ahora está en la épica [E99](E99-icebox/README.md).
