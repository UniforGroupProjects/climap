from fastapi import APIRouter, Query

from src.schemas.cidades import CidadesResponse
from src.services.brasil_api import buscar_cidades_por_uf

router = APIRouter()


@router.get(
    "/api/v1/cidades/{uf}",
    response_model=CidadesResponse,
    tags=["Cidades"]
)
def listar_cidades(
    uf: str,
    limite: int = Query(
        default=10,
        ge=1,
        le=853,
        description="Quantidade máxima de cidades"
    )
):

    return buscar_cidades_por_uf(
        uf=uf,
        limite=limite
    )