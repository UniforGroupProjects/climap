from fastapi import APIRouter

from src.schemas.clima import ClimaResponse
from src.services.open_meteo_geoloc import buscar_coordenadas
from src.services.open_meteo_clima import buscar_clima

router = APIRouter()


@router.get(
    "/api/v1/clima/{cidade}",
    response_model=ClimaResponse,
    tags=["Clima"],
    summary="Consultar clima por cidade",
    description="Retorna informações climáticas atuais com base no nome da cidade"
)
def consultar_clima(cidade: str):

    localizacao = buscar_coordenadas(cidade)

    clima = buscar_clima(
        latitude=localizacao.latitude,
        longitude=localizacao.longitude
    )

    return ClimaResponse(
        cidade=localizacao.nome,
        estado=localizacao.estado,
        temperatura_max=clima.temperatura_max,
        temperatura_min=clima.temperatura_min,
        condicao=clima.condicao
    )