from fastapi import APIRouter, HTTPException
from services.deepseek_service import DeepseekService

router = APIRouter()
deepseek_service = DeepseekService()

@router.get("/deepseek/search")
async def search(query: str):
    try:
        results = await deepseek_service.search(query)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/deepseek/details/{item_id}")
async def get_details(item_id: str):
    try:
        details = await deepseek_service.get_details(item_id)
        return details
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))