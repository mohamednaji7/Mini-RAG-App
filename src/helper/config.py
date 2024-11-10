from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_CHUNK_SIZE: int

    class Config:
        env_file=".env"

def get_settings():
    return Settings()

def get_projects_path():
    root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    return os.path.join(root, "assets", "projects")
