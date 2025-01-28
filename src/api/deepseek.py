from fastapi import APIRouter, HTTPException
from src.services.deepseek_service import DeepseekService

router = APIRouter()
deepseek_service = DeepseekService()

@router.post("/deepseek/chat")
async def chat(messages: list):
    try:
        response = deepseek_service.chat(messages)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))