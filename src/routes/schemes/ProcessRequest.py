from pydantic import BaseModel 
from typing import Optional

class ProcessRequest(BaseModel):
    file_id: str 
    chunk_size: Optional[int] = 400
    chunk_overlap_size:  Optional[int] = 20
    del_prev: Optional[int] = 0 