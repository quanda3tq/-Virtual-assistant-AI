import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "abc!123")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "assistant_ai")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")

    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

settings = Settings()
