from fastapi import FastAPI
from .routes.routes import router


#python -m uvicorn app.main:app --reload --port 8000

app = FastAPI(
    title="API prediction m² pour les maison et appartement à lille ou bordeau",
    description="API pour la prédiction de prix à lille et bordeau",
)

app.include_router(router)