from fastapi import Request
from fastapi.responses import JSONResponse
from src.core.exceptions import CidadeNaoEncontrada, NomeInvalido, UFInvalida, ServicoExternoIndisponivel

# Erro 404 - Cidade não encontrada
async def cidade_nao_encontrada_handler(request: Request, exc: CidadeNaoEncontrada):
    nome_informado = request.path_params.get("cidade", "Desconhecido")
    return JSONResponse(
        status_code=404,
        content={
            "erro": True,
            "codigo": "CIDADE_NAO_ENCONTRADA",
            "mensagem": "Nenhuma cidade encontrada com o nome informado",
            "nome_informado": nome_informado
        }
    )

# Erro 400 - UF Inválida (Sintaxe incorreta)
async def uf_invalida_handler(request: Request, exc: UFInvalida):
    sigla = request.path_params.get("uf", "Desconhecido")
    return JSONResponse(
        status_code=400,
        content={
            "erro": True,
            "codigo": "SIGLA_UF_INVALIDA",
            "mensagem": "A sigla do estado deve conter exatamente 2 letras",
            "sigla_uf_informada": sigla
        }
    )

# Erro 503 - Serviço Externo Indisponível (Se o Open-Meteo ou BrasilAPI caírem)
async def servico_indisponivel_handler(request: Request, exc: ServicoExternoIndisponivel):
    return JSONResponse(
        status_code=503,
        content={
            "erro": True,
            "codigo": "SERVICO_EXTERNO_INDISPONIVEL",
            "mensagem": "Não foi possível obter dados do serviço externo. Tente novamente em alguns instantes",
            "servico": "CPTEC"
        }
    )

async def nome_invalido_handler(
    request,
    exc: NomeInvalido
):
    return JSONResponse(
        status_code=400,
        content={
            "erro": True,
            "codigo": "NOME_INVALIDO",
            "mensagem": (
                "O nome da cidade deve conter "
                "pelo menos 2 caracteres"
            ),
            "nome_informado": exc.nome
        }
    )