from fastapi import APIRouter, UploadFile, status
from fastapi.responses import JSONResponse
from helper.config import get_settings
from controllers import DataController

app_settings = get_settings()

data_router = APIRouter(
    prefix = "/api/v1/data", #endpoint
    tags = ["api_v1", "data"],
)


@data_router.post("/upload")
async def upload(file: UploadFile ):
    is_valid, msg = DataController().validate_uploaded_file(file)
    if not is_valid:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {
                "msg": msg
            }
        )