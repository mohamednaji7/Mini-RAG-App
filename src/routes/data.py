from fastapi import APIRouter, UploadFile, status
from fastapi.responses import JSONResponse
from helper.config import get_settings, Settings
from controllers import DataController, ProjectController, ProcessController
from models import ResponseSignal
from .schemes.ProcessRequest import ProcessRequest
import os
data_router = APIRouter(
    prefix = "/api/v1/data", #endpoint
    tags = ["api_v1", "data"],
)


@data_router.post("/upload/{project_id}")
async def upload(project_id: str, file: UploadFile ):
    data_cntrlr = DataController()
    
    # Process the filename and get the project path
    project_path = ProjectController().get_project_path(project_id) 
    name, ext = data_cntrlr.processName(org_filename=file.filename)

    # Check if the file type is valid
    if not data_cntrlr.valid_file_type(file):
        status_code = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
        msg = ResponseSignal.file_type_error.value
    
    # Check if the file size is valid
    elif not data_cntrlr.valid_file_size(file):
        status_code = status.HTTP_400_BAD_REQUEST
        msg = ResponseSignal.file_size_error.value
    else:
        # Check if the file was already written
        if data_cntrlr.file_was_written(project_path, name=name, ext=ext):
            status_code = status.HTTP_409_CONFLICT
            msg = ResponseSignal.file_duplicated.value

        else:
            # Try to write the file
            done = await data_cntrlr.write_file(project_path, file)
            if done: 
                status_code = status.HTTP_200_OK
                msg = ResponseSignal.file_upload_success.value
            else:
                # File writing failed due to an internal server error
                status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
                msg = ResponseSignal.file_writting_falied.value
    
    return JSONResponse(
            status_code = status_code,
            content = {
                "details": msg,
                "file_id": data_cntrlr.get_existing_file(project_path, name, ext)

            }
        )
    
@data_router.post("/process/{project_id}") 
async def processfile(project_id: str, process_req: ProcessRequest):
    project_path = ProjectController().get_project_path(project_id) 
    data_cntrlr = DataController()
    prcs_cntrl = ProcessController()
    file_id = process_req.file_id
    name, ext = data_cntrlr.processName(file_id)
    loader = prcs_cntrl.get_file_content(project_path, file_id, ext)
    return loader, name