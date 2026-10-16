from fastapi import APIRouter

router = APIRouter(tags=["salud"])


@router.get("/health")
async def health() -> dict[str, str]:
    """Chequeo de vida para el balanceador del hosting y para CI."""
    return {"status": "ok"}
