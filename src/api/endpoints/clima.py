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
    description="Retorna o clima atual para a cidade pesquisada"
)
def consultar_clima(cidade: str):
    
    # Busca todas as localizações (já levanta erro se não achar)
    localizacoes = buscar_coordenadas(cidade)
    
    # Pegamos apenas a primeira cidade da lista
    loc = localizacoes[0]
    
    # Busca o clima usando as coordenadas
    clima = buscar_clima(
        latitude=loc.latitude,
        longitude=loc.longitude
    )
    
    return ClimaResponse(
        nome=loc.nome,
        estado=loc.estado,
        clima={
            "temperatura_min": clima.temperatura_min,
            "temperatura_max": clima.temperatura_max,
            "condicao": clima.condicao
        }
    )