from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from src.utils.datetime_utils import utc_now

class CidadeItem(BaseModel):
    nome: str

class CidadeResponse(BaseModel):  
    nome: str
    uf: str

class CidadesResponse(BaseModel):
    uf: str
    quantidade_retornada: int
    cidades: List[CidadeItem]
    consultado_em: str = Field(default_factory=utc_now)