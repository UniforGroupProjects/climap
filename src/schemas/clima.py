from datetime import datetime
from src.utils.datetime_utils import utc_now

from pydantic import BaseModel
from typing import List

class ClimaData(BaseModel):
    temperatura_max: float
    temperatura_min: float
    condicao: str

class ClimaResponse(BaseModel):
    cidade: str
    estado: str
    temperatura_max: float
    temperatura_min: float
    condicao: str

class ClimaListaResponse(BaseModel):
    quantidade: int
    resultados: List[ClimaResponse]
    data_consulta: datetime = utc_now()