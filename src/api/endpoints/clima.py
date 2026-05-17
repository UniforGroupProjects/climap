from fastapi import APIRouter, Query

from src.schemas.clima import ClimaResponse, ClimaListaResponse
from src.services.open_meteo_geoloc import buscar_coordenadas
from src.services.open_meteo_clima import buscar_clima
from src.utils.datetime_utils import utc_now

router = APIRouter()


@router.get(
    "/api/v1/clima/{cidade}",
    response_model=ClimaListaResponse,
    tags=["Clima"],
    summary="Consultar clima por cidade",
    description="Retorna todas as cidades encontradas para o nome pesquisado"
)
def consultar_clima(
    cidade: str,
    limite: int = Query(
        default=3,
        ge=1,
        le=10,
        description="Quantidade máxima de cidades retornadas"
    )
):

    localizacoes  = buscar_coordenadas(cidade)
    resultados = []

    for localizacao in localizacoes[:limite]:

        clima = buscar_clima(
            latitude=localizacao.latitude,
            longitude=localizacao.longitude
        )

        resultados.append(
            ClimaResponse(
                cidade=localizacao.nome,
                estado=localizacao.estado,
                temperatura_max=clima.temperatura_max,
                temperatura_min=clima.temperatura_min,
                condicao=clima.condicao
            )
        )

    return ClimaListaResponse(
        quantidade=len(resultados),
        resultados=resultados,
        data_consulta=utc_now()
    )