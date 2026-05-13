import requests


BASE_URL = "https://brasilapi.com.br/api/ibge/municipios/v1"


def buscar_cidades_por_uf(uf: str):
    response = requests.get(f"{BASE_URL}/{uf}")

    response.raise_for_status()

    return response.json()