#!/usr/bin/env bash
# Configura el repositorio de GitHub una sola vez, después de crearlo y hacer el primer push.
# Requiere: gh autenticado con permisos de administración sobre el repositorio.
#
# Uso:   scripts/bootstrap-github.sh jdcaballero15/Refrigeraci-n---Agus
#
# Qué hace:
#   1. Crea o actualiza las etiquetas de .github/labels.yml
#   2. Configura merge (solo squash, borrar rama al mergear)
#   3. Protege main (PR obligatorio, check ci-ok, historial lineal, sin force push)
#
# Los secretos (ANTHROPIC_API_KEY) se cargan aparte:  gh secret set ANTHROPIC_API_KEY -R <repo>

set -euo pipefail

REPO="${1:?Uso: $0 <owner>/<repo>}"

echo "==> Etiquetas"
python3 - "$REPO" <<'PY'
import subprocess, sys, yaml
repo = sys.argv[1]
with open(".github/labels.yml", encoding="utf-8") as f:
    labels = yaml.safe_load(f)
for lb in labels:
    subprocess.run(
        ["gh", "label", "create", lb["name"], "--color", lb["color"],
         "--description", lb["description"], "--force", "-R", repo],
        check=True,
    )
    print("  ok", lb["name"])
PY

echo "==> Ajustes del repositorio"
gh api -X PATCH "repos/${REPO}" \
  -F allow_squash_merge=true \
  -F allow_merge_commit=false \
  -F allow_rebase_merge=false \
  -F delete_branch_on_merge=true \
  -F allow_auto_merge=true \
  -f squash_merge_commit_title=PR_TITLE \
  -f squash_merge_commit_message=PR_BODY >/dev/null

echo "==> Protección de la rama main"
gh api -X PUT "repos/${REPO}/branches/main/protection" --input - >/dev/null <<'JSON'
{
  "required_status_checks": { "strict": true, "contexts": ["ci-ok"] },
  "enforce_admins": false,
  "required_pull_request_reviews": {
    "required_approving_review_count": 0,
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": false
  },
  "restrictions": null,
  "required_linear_history": true,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "required_conversation_resolution": true
}
JSON

echo "Listo. Pendiente a mano:"
echo "  - gh secret set ANTHROPIC_API_KEY -R ${REPO}"
echo "  - Instalar la app de GitHub de Claude: https://github.com/apps/claude"
echo "  - Reemplazar los marcadores de .github/CODEOWNERS y descomentar las líneas"
echo "  - Subir 'required_approving_review_count' a 1 cuando haya más de un desarrollador"
