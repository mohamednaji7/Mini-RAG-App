from fastapi import APIRouter
import os

base_router = APIRouter(
    prefix = "/api/v1",
    # tag = ["RAG"]
)


@base_router.get("/")
def root():

    return {
        "code": 1,
        "app_name": os.getenv('APP_NAME'),
        "app_version": os.getenv('APP_VERSION')
    }