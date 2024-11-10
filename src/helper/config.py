from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from langchain_community.document_loaders import TextLoader, PyMuPDFLoader   


class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_CHUNK_SIZE: int
    MONGODB_URL : str   
    MONGODB_DATABASE: str
    
    class Config:
        env_file=".env"

def get_settings():
    return Settings()

def get_projects_path():
    root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    return os.path.join(root, "assets", "projects")

def get_loader(ext):
    return {
        ".txt": TextLoader,
        ".pdf": PyMuPDFLoader,
    }[ext]