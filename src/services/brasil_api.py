import requests
from src.utils.validators import UFS_VALIDAS

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


def _buscar_cidades_raw(uf: str):

    try:

        response = requests.get(
            f"{BRASIL_API_URL}/{uf}",
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        return response.json()

    except RequestException:
        raise ServicoExternoIndisponivel()

def buscar_cidades_por_uf(
    uf: str,
    limite: int
) -> CidadesResponse:

    uf = uf.upper()

    if not validar_uf(uf):
        raise UFInvalida()

    cidades_data = _buscar_cidades_raw(uf)

    nomes_cidades = [
        cidade["nome"]
        for cidade in cidades_data[:limite]
    ]

    return CidadesResponse(
        uf=uf,
        quantidade=len(nomes_cidades),
        cidades=nomes_cidades
    )

def buscar_cidades_por_nome(nome: str):

    nome = nome.lower().strip()

    resultados = []

    for uf in UFS_VALIDAS:

        cidades_data = _buscar_cidades_raw(uf)

        for cidade in cidades_data:

            cidade_nome = cidade["nome"]

            if cidade_nome.lower().startswith(nome):

                resultados.append({
                    "nome": cidade_nome,
                    "uf": uf
                })

    return resultados