import requests

from src.schemas.geoloc import GeocodingResponse
from src.core.exceptions import CidadeNaoEncontrada


BASE_URL = "https://geocoding-api.open-meteo.com/v1/search"


def buscar_coordenadas(cidade: str) -> GeocodingResponse:
    response = requests.get(
        BASE_URL,
        params={
            "name": cidade,
            "count": 1,
            "language": "pt",
            "format": "json"
        },
        timeout=10
    )

    response.raise_for_status()

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