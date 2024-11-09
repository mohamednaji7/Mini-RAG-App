from fastapi import APIRouter
from helper.config import get_settings

app_settings = get_settings()

base_router = APIRouter(
    prefix = "/api/v1",
    tags = ["api_v1", "root"],
)


@base_router.get("/")
async def root():
    return {
        "code": 1,
        "app_name": app_settings.APP_NAME,
        "app_version": app_settings.APP_VERSION
    }