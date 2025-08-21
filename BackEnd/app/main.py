from fastapi import FastAPI
from app.routes import auth, chat, voice

app = FastAPI(title="AI Assistant API")

# Register routes
app.include_router(auth.router)
app.include_router(chat.router)
app.include_router(voice.router)

@app.get("/")
def root():
    return {"message": "AI Assistant Backend is running 🚀"}
