from fastapi import APIRouter

from src.schemas.health import HealthResponse
from src.utils.datetime_utils import utc_now

router = APIRouter()


@router.get(
    "/api/v1/health",
    response_model=HealthResponse,
    tags=["Health"]
)
def health_check():
    return HealthResponse(
        status="healthy",
        timestamp=utc_now()
    )