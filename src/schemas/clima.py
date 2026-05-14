from pydantic import BaseModel


class ClimaData(BaseModel):
    temperatura_max: float
    temperatura_min: float
    condicao: str