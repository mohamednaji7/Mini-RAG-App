from enum import Enum 

class ResponseSignal(Enum):
    file_type_not_supported = "File Type Not Supported"
    file_size_exceeded = "File Size Exceeded"
    upload_sucess = "File Uploaded Succesfully"
    upload_falied = "File Upload Falied"
    file_validated = "File got  Valdiated"