from pydantic import BaseModel
from typing import List


class CidadesResponse(BaseModel):
    uf: str
    quantidade: int
    cidades: List[str]

class CidadeResponse(BaseModel):
    nome: str
    uf: str