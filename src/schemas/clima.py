from pydantic import BaseModel, Field
from src.utils.datetime_utils import utc_now

class UnidadesClima(BaseModel):
    temperatura: str = "°C"

class ClimaDetalhe(BaseModel):
    temperatura_min: float
    temperatura_max: float
    condicao: str
    unidades: UnidadesClima = UnidadesClima()

class ClimaResponse(BaseModel):
    nome: str
    estado: str
    clima: ClimaDetalhe
    consultado_em: str = Field(default_factory=utc_now)