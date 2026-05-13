from pydantic import BaseModel


class GeocodingResponse(BaseModel):
    nome: str
    estado: str
    latitude: float
    longitude: float