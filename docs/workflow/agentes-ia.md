# Trabajar con agentes de IA

Hay dos formas de usar IA en este repositorio. Ambas leen las mismas reglas (`CLAUDE.md`) y están versionadas.

## 1. Agentes de desarrollo (Claude Code, en tu máquina)

Abrí Claude Code en la raíz del repo. Vas a encontrar:

| Qué | Dónde | Para qué |
|---|---|---|
| Contexto y reglas | `CLAUDE.md`, `AGENTS.md` | Lo lee cualquier agente al arrancar |
| Permisos | `.claude/settings.json` | Qué comandos se permiten y cuáles se niegan (sin `.env`, sin force push, sin merge) |
| Subagentes | `.claude/agents/` | `backend-dev`, `frontend-dev`, `db-migrations`, `story-writer`, `qa-reviewer` |
| Comandos | `.claude/commands/` | `/implement-story`, `/new-story`, `/review-story`, `/new-migration`, `/resolve-decision` |

### Flujo recomendado

```
/new-story <pedido>         -> historia en borrador
/review-story E04-03        -> la revisás, negocio la valida y pasa a ready
/implement-story E04-03     -> rama, tests, código, PR
```

Cuando el cliente responde una decisión pendiente: `/resolve-decision D-001 <respuesta>`.

### Cómo sacarles provecho

- Una historia por sesión. Contexto chico, resultados mejores.
- Si el agente frena porque la historia está bloqueada o en borrador, es correcto: el problema es la historia.
- Pedile `qa-reviewer` antes de abrir el PR.
- Las reglas de dominio están en `CLAUDE.md`. Si aparece una regla nueva, se agrega ahí, no se repite en cada pedido.

## 2. Automatización en GitHub (Actions)

| Workflow | Cuándo corre | Qué hace |
|---|---|---|
| `claude-review.yml` | PR nuevo o actualizado (de ramas del repo, no forks) | Revisa contra reglas de dominio, historia, seguridad y migraciones. Comenta en línea |
| `claude.yml` | Alguien con permiso de escritura menciona `@claude` en un issue o PR | Responde, implementa una historia o corrige un PR |
| `claude-triage.yml` | Issue nuevo | Verifica formato, aplica etiquetas, avisa si hay datos sensibles |
| `stories-sync.yml` | Push a `main` que toca `docs/stories/` | Crea o actualiza issues desde las historias |

### Puesta en marcha (una sola vez)

1. Instalar la [app de GitHub de Claude](https://github.com/apps/claude) en el repositorio.
2. Cargar el secreto: `gh secret set ANTHROPIC_API_KEY -R MendoData/ot-platform`.
3. Correr `scripts/bootstrap-github.sh MendoData/ot-platform` (etiquetas, ajustes de merge y protección de `main`).

### Ejemplos

```
@claude implementá esta historia siguiendo CLAUDE.md
@claude revisá si este PR respeta que el técnico no vea precios
@claude explicá por qué falla el check backend
```

### Límites y seguridad

- Solo colaboradores con permiso de escritura activan a Claude. No corre sobre PR de forks.
- Claude nunca hace merge ni despliega: abre PR y una persona aprueba.
- Permisos mínimos en cada workflow (`permissions:`) y lista de herramientas acotada (`--allowedTools`).
- La clave vive en GitHub Secrets. Los agentes no la leen.
- Cada ejecución tiene límite de turnos (`--max-turns`) y de tiempo (`timeout-minutes`) para acotar el costo.
- Revisá el uso en la consola de Anthropic y poné un tope de gasto mensual.

## Qué no hacen los agentes

- No cambian el alcance ni inventan requisitos: si falta información, preguntan o crean una decisión pendiente.
- No tocan secretos, protección de ramas ni producción.
- No reemplazan la validación de negocio de las historias.

## Fuera de alcance por ahora

Agentes de IA dentro del producto (resumir historial de un equipo, sugerir fallas desde observaciones). Ver `E99-03`.
