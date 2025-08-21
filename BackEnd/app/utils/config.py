import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Database
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    # OpenAI
    OPENAI_API_KEY: str = ""

    # App
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    DEBUG: bool = True

    # PgAdmin
    PGADMIN_DEFAULT_EMAIL: str = "admin@example.com"
    PGADMIN_DEFAULT_PASSWORD: str = "admin"

    class Config:
        env_file = ".env"   # Load từ file .env trong thư mục gốc

# Singleton settings
settings = Settings()
