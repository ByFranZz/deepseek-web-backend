import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from src.api.deepseek import router as deepseek_router

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

app = FastAPI()

# Configuración de CORS
origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(deepseek_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Deepseek API backend!"}