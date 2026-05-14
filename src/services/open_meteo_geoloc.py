import requests

from src.schemas.geoloc import GeocodingResponse
from src.core.exceptions import CidadeNaoEncontrada, ServicoExternoIndisponivel
from requests.exceptions import RequestException

from src.core.config import (
    GEOCODING_BASE_URL,
    REQUEST_TIMEOUT
)


def buscar_coordenadas(cidade: str) -> GeocodingResponse:
    try:
        response = requests.get(
            GEOCODING_BASE_URL,
            params={
                "name": cidade,
                "count": 1,
                "language": "pt",
                "format": "json"
            },
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

    except RequestException:
        raise ServicoExternoIndisponivel()
    
    data = response.json()

    resultados = data.get("results")

    if not resultados:
        raise CidadeNaoEncontrada()

    cidade_data = resultados[0]

    return GeocodingResponse(
        nome=cidade_data["name"],
        estado=cidade_data.get("admin1", ""),
        latitude=cidade_data["latitude"],
        longitude=cidade_data["longitude"]
    )