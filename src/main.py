from fastapi import FastAPI
from src.api.router import router


from src.core.exceptions import CidadeNaoEncontrada, NomeInvalido, UFInvalida, ServicoExternoIndisponivel
from src.core.handlers import (
    cidade_nao_encontrada_handler,
    nome_invalido_handler,
    uf_invalida_handler,
    servico_indisponivel_handler
)

app = FastAPI(
    title="Climap API",
    version="1.0.0",
    description="API de consulta climática e geográfica"
)

app.include_router(router)


app.add_exception_handler(CidadeNaoEncontrada, cidade_nao_encontrada_handler)
app.add_exception_handler(UFInvalida, uf_invalida_handler)
app.add_exception_handler(ServicoExternoIndisponivel, servico_indisponivel_handler)
app.add_exception_handler(NomeInvalido, nome_invalido_handler)

@app.get("/")
def root():
    return {"message": "API funcionando"}