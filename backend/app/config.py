import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "GameNet Management System"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "gamenet_super_secret_jwt_key_2025_persian_gaming")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./gamenet.db")

    class Config:
        case_sensitive = True

settings = Settings()
