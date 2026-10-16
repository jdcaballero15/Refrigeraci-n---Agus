# ADR 0008: Agentes de IA en el repositorio

**Estado:** Aceptado

## Contexto

Se quiere acelerar el desarrollo y sostener la calidad con agentes de IA, con el repositorio público y datos personales de por medio.

## Decisión

Dos niveles, ambos versionados en el repo:

**1. Agentes de desarrollo (Claude Code)**
- `CLAUDE.md` con las reglas de dominio, comandos y convenciones. Es la fuente de contexto para cualquier agente.
- `AGENTS.md` apunta a `CLAUDE.md` para herramientas que leen ese nombre.
- `.claude/agents/`: subagentes especializados (backend, frontend, historias, base de datos, revisión).
- `.claude/commands/`: comandos reutilizables (`/implement-story`, `/new-story`, `/review-story`, `/new-migration`).
- `.claude/settings.json`: permisos mínimos compartidos.

**2. Automatización en GitHub (GitHub Actions con Claude)**
- Revisión automática de cada PR contra las reglas de dominio.
- Menciones `@claude` en issues y PR para implementar historias o responder dudas.
- Triage de issues nuevos (formato, etiquetas, datos sensibles).

**Límites**
- Solo colaboradores con permiso de escritura pueden activar a Claude. Sin PR de forks.
- Claude nunca hace merge ni despliega. Abre PR y una persona aprueba.
- Los secretos viven en GitHub Secrets. Los agentes no los leen ni los escriben.
- El agente no inventa requisitos: si falta información, lo pregunta o lo deja como decisión pendiente.

## Fuera de alcance por ahora

Agentes dentro del producto (por ejemplo, resumir el historial de un equipo o sugerir fallas desde observaciones). Se evalúa cuando el circuito base esté en producción. Queda como historia `E99-03` en el icebox.

## Consecuencias

- El contexto del proyecto se mantiene en archivos revisables, no en la cabeza de una persona.
- El costo de la API de Anthropic en CI es un gasto del proyecto. Se acotan turnos y tiempos en cada workflow.
