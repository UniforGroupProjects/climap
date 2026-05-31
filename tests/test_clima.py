from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_clima_cidade_inexistente():
    response = client.get("/api/v1/clima/CidadeFalsaDoGrupo123")
    assert response.status_code == 404
    data = response.json()
    assert data["erro"] is True
    assert data["codigo"] == "CIDADE_NAO_ENCONTRADA"