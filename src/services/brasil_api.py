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

from src.schemas.cidades import CidadesResponse, CidadeResponse

from src.utils.validators import validar_uf

from requests.exceptions import HTTPError, Timeout


def _buscar_cidades_raw(uf: str):

    try:

        response = requests.get(
            f"{BRASIL_API_URL}/{uf}",
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

    except (Timeout, ConnectionError):
        raise ServicoExternoIndisponivel()

    except HTTPError as error:

        if error.response.status_code == 404:
            raise UFInvalida()

        raise ServicoExternoIndisponivel()

    return response.json()


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

    # --- MUDANÇA FEITA AQUI ---
    return CidadesResponse(
        uf=uf,
        quantidade_retornada=len(nomes_cidades),
        cidades=[{"nome": nome} for nome in nomes_cidades]
    )


def buscar_cidades_por_nome(nome: str):

    nome = nome.lower().strip()

    resultados = []

    for uf in UFS_VALIDAS:

        cidades_data = _buscar_cidades_raw(uf)

        for cidade in cidades_data:

            cidade_nome = cidade["nome"]

            if cidade_nome.lower().startswith(nome):

                resultados.append(
                    CidadeResponse(
                        nome=cidade_nome,
                        uf=uf
                    )
                )

    return resultados