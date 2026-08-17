from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.api.routes import router

app = FastAPI(title="JurisAO API", description="Agente de IA sobre legislação angolana")
app.include_router(router)
app.mount("/", StaticFiles(directory="static", html=True), name="static")