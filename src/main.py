from fastapi import FastAPI

from src.api.router import router

app = FastAPI(
    title="Climap API",
    version="1.0.0",
    description="API de consulta climática e geográfica"
)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "API funcionando"}