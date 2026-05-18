import requests

from src.schemas.clima import ClimaDetalhe
from src.utils.formatters import traduzir_weather_code
from requests.exceptions import RequestException
from src.core.exceptions import ServicoExternoIndisponivel

from src.core.config import (
    OPEN_METEO_BASE_URL,
    REQUEST_TIMEOUT
)

def buscar_clima(
    latitude: float,
    longitude: float
) -> ClimaDetalhe:

    try:
        response = requests.get(
            OPEN_METEO_BASE_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "daily": (
                    "temperature_2m_max,"
                    "temperature_2m_min,"
                    "weathercode"
                ),
                "timezone": "auto"
            },
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

    except RequestException:
        raise ServicoExternoIndisponivel()

    data = response.json()

    daily = data["daily"]

    weather_code = daily["weathercode"][0]

    return ClimaDetalhe(
        temperatura_max=daily["temperature_2m_max"][0],
        temperatura_min=daily["temperature_2m_min"][0],
        condicao=traduzir_weather_code(weather_code)
    )