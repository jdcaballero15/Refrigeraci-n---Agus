# ADR NNNN: <Titulo en una linea, imperativo>

- **Estado:** Propuesto | Provisional | Aceptado | Rechazado | Reemplazado por ADR NNNN
- **Fecha:** AAAA-MM-DD
- **Decide:** <rol responsable>
- **Áreas afectadas:** <backend | web-admin | pwa-tecnico | datos | infra | docs | ia>

---

## Contexto

Qué problema hay que resolver y por qué **ahora**. Restricciones reales: plazos, conocimiento
del equipo, costo, legales (Ley 25.326), límites del cliente. Se escribe sin mencionar la solución.

## Decisión

Qué se decidió, en una o dos frases, en presente:

> Usamos X para Y.

Después, el detalle necesario para implementarlo sin volver a preguntar.

## Alternativas consideradas

| Alternativa | Ventajas | Por qué se descartó |
|---|---|---|
| A | | |
| B | | |

Si esta tabla está vacía, el ADR no está listo.

## Consecuencias

**Positivas**
-

**Negativas o costo que aceptamos**
-

**Qué se vuelve más difícil de ahora en adelante**
-

## Impacto en las reglas del repositorio

Marcá lo que haya que actualizar y hacelo en el mismo PR.

- [ ] [`CLAUDE.md`](../../../CLAUDE.md): reglas o estructura
- [ ] [`docs/code-standards.md`](../../code-standards.md)
- [ ] `ALLOWED_TOPLEVEL` en `.claude/hooks/guard_edit.py` (carpeta nueva en la raíz)
- [ ] `.github/workflows/ci.yml`
- [ ] `.env.example`
- [ ] Historias afectadas en `docs/stories/`
- [ ] Ninguno

## Referencias

- Enlaces a documentación, PR, historias (`EXX-NN`), decisiones pendientes (`D-0XX`) u otros ADR.
