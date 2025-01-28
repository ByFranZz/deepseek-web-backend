from fastapi import FastAPI
from src.api.deepseek import router as deepseek_router

app = FastAPI()

app.include_router(deepseek_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Deepseek API backend!"}