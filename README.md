# 🌦️ Climap API

API REST desenvolvida em **Python + FastAPI** para consulta de clima em cidades brasileiras.

O projeto integra:

* 🇧🇷 **BrasilAPI** para localização e validação de cidades brasileiras
* 🌍 **Open-Meteo Geocoding API** para obtenção de coordenadas geográficas
* ☁️ **Open-Meteo Weather API** para consulta das condições climáticas

---

# 🚀 Funcionalidades

✅ Listar cidades por UF

✅ Buscar cidades por nome

✅ Consultar clima de cidades brasileiras

✅ Validação de entradas

✅ Tratamento padronizado de erros

✅ Testes automatizados

✅ Collection Postman para testes da API

---

# 🛠️ Tecnologias Utilizadas

* 🐍 Python 3.10+
* ⚡ FastAPI
* 📦 Pydantic
* 🌐 Requests
* 🧪 Pytest
* 📮 Postman

---

# 📁 Estrutura do Projeto

```text
.
├── README.md
├── INTEGRANTES.md
├── docs
│   └── postman_collection.json
├── src
│   ├── api
│   ├── core
│   ├── schemas
│   ├── services
│   └── utils
└── tests
```

---

# ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/climap.git
```

Acesse a pasta:

```bash
cd climap
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# ▶️ Executando a Aplicação

```bash
uvicorn src.main:app --reload --port 3000
```

Servidor disponível em:

```text
http://localhost:3000
```

---

# 📚 Documentação Swagger

Após iniciar a aplicação:

🔗 Swagger UI

```text
http://localhost:3000/docs
```

🔗 ReDoc

```text
http://localhost:3000/redoc
```

---

# 🌎 Endpoint de Cidades

## Buscar cidades por UF

```http
GET /api/v1/cidades/{uf}
```

### Exemplo

```http
GET /api/v1/cidades/CE
```

### Resposta

```json
{
  "uf": "CE",
  "quantidade_retornada": 10,
  "cidades": [
    {
      "nome": "ABAIARA"
    }
  ],
  "consultado_em": "2026-06-05T18:00:00+00:00"
}
```

---

# ☁️ Endpoint de Clima

## Consultar clima por cidade

```http
GET /api/v1/clima/{cidade}
```

### Exemplo

```http
GET /api/v1/clima/Fortaleza
```

### Resposta

```json
{
  "nome": "FORTALEZA",
  "estado": "CE",
  "clima": {
    "temperatura_min": 25.3,
    "temperatura_max": 31.8,
    "condicao": "Parcialmente nublado",
    "unidades": {
      "temperatura": "°C"
    }
  },
  "consultado_em": "2026-06-05T18:00:00+00:00"
}
```

---

# ❌ Tratamento de Erros

## Cidade não encontrada

```json
{
  "erro": true,
  "codigo": "CIDADE_NAO_ENCONTRADA",
  "mensagem": "Nenhuma cidade encontrada com o nome informado",
  "nome_informado": "CidadeTeste"
}
```

---

## Nome inválido

```json
{
  "erro": true,
  "codigo": "NOME_INVALIDO",
  "mensagem": "O nome da cidade deve conter pelo menos 2 caracteres",
  "nome_informado": "X"
}
```

---

## Serviço externo indisponível

```json
{
  "erro": true,
  "codigo": "SERVICO_EXTERNO_INDISPONIVEL",
  "mensagem": "Não foi possível obter dados do serviço externo. Tente novamente em alguns instantes"
}
```

---

# 🧪 Executando os Testes

Rodar todos os testes:

```bash
pytest
```

Exibir cobertura:

```bash
pytest -v
```

---

# 📮 Collection Postman

A collection utilizada para testes da API encontra-se em:

```text
docs/postman_collection.json
```

Para importar:

1. Abra o Postman 📮
2. Clique em **Import**
3. Selecione `postman_collection.json`
4. Execute as requisições e testes

---

# 👥 Equipe

Informações dos integrantes disponíveis em:

```text
INTEGRANTES.md
```

---

# Integrantes da Equipe

| Nome Completo             | Matrícula | Papel                 |
|---------------------------|-----------|-----------------------|
| Daniel Silva Gomes        | 2416870   | Desenvolvedor Backend |
| Cintia de Freitas Neves   | 2415499   | Desenvolvedor Backend |

---

# 🎯 Objetivo Acadêmico

Projeto desenvolvido para a disciplina de **Técnicas de Integração de Sistemas** do curso de Análise e Desenvolvimento de Sistemas na Universidade de Fortaleza - UNIFOR, aplicando conceitos de:

* 📐 Arquitetura em camadas
* 🔄 Integração com APIs externas
* 🧩 Tratamento de exceções
* 🧪 Testes automatizados
* 📚 Documentação de APIs
* 🚀 Boas práticas com FastAPI

---

⭐ Se este projeto foi útil para você, considere deixar uma estrela no repositório!
