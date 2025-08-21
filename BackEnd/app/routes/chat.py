from fastapi import APIRouter
from app.services.openai_service import ask_chatgpt

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/")
def chat(message: str):
    response = ask_chatgpt(message)
    return {"response": response}
