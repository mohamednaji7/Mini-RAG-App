from enum import Enum 

class ResponseSignal(Enum):
    file_type_error = "File Type Not Supported"
    file_size_error = "File Size Exceeded"
    file_upload_success = "File Uploaded Succesfully"
    file_writting_falied = "Failed to write the file due to an internal server error."
    file_duplicated = "File Already Uploaded"