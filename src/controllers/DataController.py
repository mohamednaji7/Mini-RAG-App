from fastapi import UploadFile
from .BaseController import BaseController
from models.enums import ResponseSignal 



class DataController(BaseController):
    def __init__(self):
        super().__init__()
    
    def validate_uploaded_file(self, file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.file_type_not_supported.value
        if file.size > self.app_settings.FILE_MAX_SIZE*1048576: #1048576  1Mbyte
            return False, ResponseSignal.file_size_exceeded.value
        return True, ResponseSignal.file_validated.value