from pydantic import BaseModel

class HealthResponse(BaseModel):
    status: str
    versao: str = "1.0.0" 
    timestamp: str