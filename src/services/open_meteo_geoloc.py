import requests

from src.schemas.geoloc import GeocodingResponse
from src.core.exceptions import CidadeNaoEncontrada, NomeInvalido, ServicoExternoIndisponivel
from requests.exceptions import RequestException
from src.services.brasil_api import buscar_cidades_por_nome

from src.core.config import (
    GEOCODING_BASE_URL,
    REQUEST_TIMEOUT
)


def buscar_coordenadas(
    cidade: str
) -> list[GeocodingResponse]:


    cidade = cidade.strip()

    if len(cidade) < 2:
        raise NomeInvalido(cidade)

    cidades_brasileiras = buscar_cidades_por_nome(cidade)

    if not cidades_brasileiras:
        raise CidadeNaoEncontrada()

    coordenadas = []

    for cidade_brasileira in cidades_brasileiras:

        query = cidade_brasileira.nome

        try:

            response = requests.get(
                GEOCODING_BASE_URL,
                params={
                    "name": query,
                    "count": 10,
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
            continue

        item = resultados[0]

        coordenadas.append(
            GeocodingResponse(
                nome=cidade_brasileira.nome,
                estado=cidade_brasileira.uf,
                latitude=item["latitude"],
                longitude=item["longitude"]
            )
        )

    if not coordenadas:
        raise CidadeNaoEncontrada()

    return coordenadas