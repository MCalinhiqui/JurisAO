from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(title="LegisAgent API", description="Agente de IA sobre legislação angolana")
app.include_router(router)