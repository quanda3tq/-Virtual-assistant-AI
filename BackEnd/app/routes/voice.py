from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/voice", tags=["Voice"])

class VoiceRequest(BaseModel):
    text: str

@router.post("/tts")
async def text_to_speech(req: VoiceRequest):
    # Thực tế: gọi API TTS (VD: gTTS hoặc OpenAI TTS)
    return {"msg": "Voice generated successfully", "text": req.text}
