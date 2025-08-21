from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, chat, voice
from app.utils.logger import logger
from app.utils.config import settings


from app.utils.config import settings
from app.utils.logger import logger

# Import routers
from app.routes import auth, chat, voice

# Khởi tạo FastAPI
app = FastAPI(
    title="AI Assistant Backend",
    description="Backend service cho Virtual Assistant AI",
    version="1.0.0"
)

# CORS Middleware (cho phép frontend gọi API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # có thể giới hạn ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Đăng ký các router
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(voice.router, prefix="/voice", tags=["Voice"])


@app.on_event("startup")
async def startup_event():
    logger.info("🚀 Application starting up...")
    logger.info(f"Database host: {settings.POSTGRES_HOST}, DB: {settings.POSTGRES_DB}")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("🛑 Application shutting down...")



app = FastAPI(title="Assistant AI Backend", debug=settings.DEBUG)

# Đăng ký router
app.include_router(auth.router)
app.include_router(chat.router)
app.include_router(voice.router)

@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {"msg": "Welcome to Assistant AI API"}