from fastapi import APIRouter, HTTPException, Query

from src.schemas.cidades import CidadesResponse
from src.services.brasil_api import buscar_cidades_por_uf
from src.utils.validators import validar_uf

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
    uf = uf.upper()

    if not validar_uf(uf):
        raise HTTPException(
            status_code=400,
            detail="UF inválida ou inexistente"
        )

    cidades_data = buscar_cidades_por_uf(uf)

    nomes_cidades = [
        cidade["nome"]
        for cidade in cidades_data[:limite]
    ]

    return CidadesResponse(
        uf=uf,
        quantidade=len(nomes_cidades),
        cidades=nomes_cidades
    )