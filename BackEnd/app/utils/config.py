import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ==== DATABASE CONFIG ====
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    # ==== PGADMIN CONFIG ====
    PGADMIN_DEFAULT_EMAIL: str
    PGADMIN_DEFAULT_PASSWORD: str

    # ==== OPENAI CONFIG ====
    OPENAI_API_KEY: str | None = None

    # ==== APP CONFIG ====
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    DEBUG: bool = True

    # Cấu hình load từ file .env
    model_config = SettingsConfigDict(
        env_file="../.env",
        env_file_encoding="utf-8",
    )


# Singleton settings (import ra toàn project)
settings = Settings()
