from fastapi import APIRouter, UploadFile, status, Depends
from fastapi.responses import JSONResponse
from helper.config import get_settings, Settings
from controllers import DataController
from models.enums import ResponseSignal 
import aiofiles, logging

logger = logging.getLogger('uvicorn.error')

app_settings = get_settings()

data_router = APIRouter(
    prefix = "/api/v1/data", #endpoint
    tags = ["api_v1", "data"],
)


@data_router.post("/upload/{project_id}")
async def upload(project_id: str, file: UploadFile,
                 app_settings: Settings = Depends(get_settings) ):
    data_cntrlr = DataController()
    is_valid, msg = data_cntrlr.validate_uploaded_file(file)
    file_path = data_cntrlr.get_unique_path(file.filename,
                                            project_id=project_id)
    
    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
        logger.error("Error while writng the file: {e}")
        return JSONResponse(
            status_code = status.HTTP_40_BAD_REQUEST,
            content = {
                "msg": ResponseSignal.upload_failed.value
            }
        )

    if not is_valid:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {
                "msg": msg
            }
        )
    else:
        return{
            "file name": file.filename,
            "file path": file_path
        }