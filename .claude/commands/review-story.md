---
description: Revisa la calidad de una historia (formato, criterios, alcance, dependencias) antes de pasarla a ready
argument-hint: <ID de la historia, por ejemplo E05-02>
---

Revisá la historia **$ARGUMENTS** sin modificarla. Usá el subagente `story-writer` en modo revisión.

Verificá:

1. **Formato**: encabezado completo, "Como / quiero / para", criterios, notas. `make stories-validate` pasa.
2. **Tamaño**: ¿entra en un PR chico? Si no, proponé cómo dividirla.
3. **Criterios**: ¿cada uno es verificable con un test? ¿hay caso de error y de permiso denegado? ¿Dice explícitamente que el técnico no ve precios, mano de obra ni historial, si el técnico participa?
4. **Alcance**: ¿contradice `docs/domain/alcance-fase-1.md` o toca algo fuera de alcance?
5. **Dependencias**: ¿`depends_on` y `blocked_by` correctos? ¿Depende de algo que no existe?
6. **Consistencia**: ¿usa el vocabulario del glosario, los estados de `order-state-machine.md` y los roles de `roles-permisos.md`?

Entregá una lista de problemas ordenada por gravedad y un veredicto: lista para `ready`, ajustes menores o necesita rehacerse.
