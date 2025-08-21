from fastapi import APIRouter

router = APIRouter(prefix="/voice", tags=["Voice"])

@router.post("/to-text")
def voice_to_text(audio_file: str):
    # TODO: convert audio -> text
    return {"text": "Xin chào (mock)"}
