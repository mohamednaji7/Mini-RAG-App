from fastapi import UploadFile, status
from fastapi.responses import JSONResponse
from .BaseController import BaseController
from .ProjectController import ProjectController
from helper.config import get_settings
from models.enums import ResponseSignal 
import re, uuid, os
import aiofiles, logging

logger = logging.getLogger('uvicorn.error')
app_settings = get_settings()

class DataController(BaseController):
    def __init__(self):
        super().__init__()
    
    def valid_file_type(self, file: UploadFile) -> bool:
        return file.content_type in self.app_settings.FILE_ALLOWED_TYPES

    def valid_file_size(self, file: UploadFile) -> bool:
        return file.size < self.app_settings.FILE_MAX_SIZE*1048576 #1048576  1Mbyte
            
    def processName(self, org_filename: str) -> tuple:
        filename = re.sub(r'[^\w.]', '', org_filename).replace(" ", "_")
        splited_fname = filename.split(".")
        ext = "."+splited_fname[-1]
        name = "".join(splited_fname[:-1])  
        return name, ext
    
    def get_unique_path(self, project_path: str, name: str, ext:str):
        while True:
            file_id = name + "_" + uuid.uuid1().hex + ext
            un_file_path = os.path.join(project_path, file_id)
            if not os.path.exists(un_file_path):
                return un_file_path
    
    def get_existing_file(self, project_path: str, name: str, ext: str) -> str:
        return next((f for f in os.listdir(project_path) if re.match(rf"^{name}_([a-f0-9\-]+){ext}$", f)), None ) # Default to None if no match is found 

    def file_was_written(self, project_path: str, name: str, ext: str) -> bool:
        return self.get_existing_file(project_path, name, ext) is not None 
        # return any(re.match(rf"^{name}_([a-f0-9\-]+){ext}$", f) for f in os.listdir(project_path))

    async def write_file(self, project_path: str, file: UploadFile)->tuple:
        name, ext = self.processName(file.filename)
        file_path = self.get_unique_path(project_path, name, ext)
        try:
            async with aiofiles.open(file_path, "wb") as f:
                while chunk := await file.read(app_settings.FILE_CHUNK_SIZE):
                    await f.write(chunk)
                return True, 
        except Exception as e:
            logger.error(f"Error while writng the file: {e}")
            return False

                  