import requests

from src.core.config import (
    BRASIL_API_URL,
    REQUEST_TIMEOUT
)

from src.core.exceptions import (
    UFInvalida,
    ServicoExternoIndisponivel
)

from src.schemas.cidades import CidadesResponse

from src.utils.validators import validar_uf

from requests.exceptions import RequestException


def buscar_cidades_por_uf(
    uf: str,
    limite: int
) -> CidadesResponse:

    uf = uf.upper()

    if not validar_uf(uf):
        raise UFInvalida()

    try:

        response = requests.get(
            f"{BRASIL_API_URL}/{uf}",
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

    except RequestException:
        raise ServicoExternoIndisponivel()

    cidades_data = response.json()

    nomes_cidades = [
        cidade["nome"]
        for cidade in cidades_data[:limite]
    ]

    return CidadesResponse(
        uf=uf,
        quantidade=len(nomes_cidades),
        cidades=nomes_cidades
    )