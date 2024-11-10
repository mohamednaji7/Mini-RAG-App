from .BaseController import BaseController
from langchain_community.document_loaders import TextLoader, PyMuPDFLoader   
from helper.config import get_loader
import os


class ProcessController(BaseController):
    def __init__(self):
        super().__init__()

    def get_file_content(self, project_path: str, file_id: str, ext: str):
        loader = get_loader(ext)(os.path.join(project_path, file_id))
        return loader.load()

        