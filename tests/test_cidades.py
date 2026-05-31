from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_buscar_cidades_sucesso():
    response = client.get("/api/v1/cidades/CE?limite=2")
    assert response.status_code == 200
    data = response.json()
    assert data["uf"] == "CE"
    assert data["quantidade_retornada"] <= 2
    assert isinstance(data["cidades"], list)

def test_buscar_cidades_uf_invalida():
    response = client.get("/api/v1/cidades/XYZ")
    assert response.status_code == 400
    data = response.json()
    assert data["erro"] is True
    assert data["codigo"] == "SIGLA_UF_INVALIDA"
    assert data["sigla_uf_informada"] == "XYZ"