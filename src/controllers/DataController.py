from fastapi import UploadFile
from .BaseController import BaseController
from .ProjectController import ProjectController
from models.enums import ResponseSignal 
import re, uuid, os


class DataController(BaseController):
    def __init__(self):
        super().__init__()
    
    def validate_uploaded_file(self, file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.file_type_not_supported.value
        if file.size > self.app_settings.FILE_MAX_SIZE*1048576: #1048576  1Mbyte
            return False, ResponseSignal.file_size_exceeded.value
        return True, ResponseSignal.file_validated.value
    
    def get_unique_path(self, org_filename:str, project_id:str):
        project_path = ProjectController().get_project_path(project_id)

        filename = re.sub(r'[^\w.]', '', org_filename).replace(" ", "_")
        splited_fname = filename.split(".")
        ext = "."+splited_fname[-1]
        name = "".join(splited_fname[:-1])        

        while True:
            un_file_path = os.path.join(
                project_path, name+"_"+str(uuid.uuid1()) + ext)
            if not os.path.exists(un_file_path):
                return un_file_path