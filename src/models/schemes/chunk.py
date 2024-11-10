from pydantic import BaseModel, Field, validator 
from typing import Optional 
from bson.objectid import ObjectId

class DataChunk(BaseModel):
    _id: Optional[ObjectId] 
    chunk_metadata: dict 
    chunk_project_id: Optional[ObjectId]
    chunk_text: str = Field(..., min_length=1)
    chunk_number: int = Field(..., gt=0)
    
    class Config: 
        arbitrary_types_allowed = True 