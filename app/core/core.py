from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    DB_URL: str = 'postgresql+asyncpg://user:root@db/urls'


settings = Settings()
