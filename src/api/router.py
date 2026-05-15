from fastapi import APIRouter

from src.api.endpoints.health import router as health_router
from src.api.endpoints.cidades import router as cidades_router
from src.api.endpoints.clima import router as clima_router

router = APIRouter()

router.include_router(health_router)
router.include_router(cidades_router)
router.include_router(clima_router)