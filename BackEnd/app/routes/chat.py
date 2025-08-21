from fastapi import APIRouter
from pydantic import BaseModel
from app.services.openai_service import ask_openai

router = APIRouter(prefix="/chat", tags=["Chat"])

class ChatRequest(BaseModel):
    message: str

@router.post("/")
async def chat(req: ChatRequest):
    response = await ask_openai(req.message)
    return {"response": response}
