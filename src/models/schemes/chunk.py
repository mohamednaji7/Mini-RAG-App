from pydantic import BaseModel, Field, validator 
from typing import Optional 
from bson.objectid import ObjectID

class DataChunk(BaseModel):
    _id: Optional[ObjectID] 
    chunk_metadata: dict 
    chunk_project_id = ObjectID
    chunk_text: str = Field(..., min_length=1)
    chunk_number: int = Field(..., gt=0)

    @validator("project_id")
    def validate(cls, value):
        if not value.isalnum():
            raise ValueError("project_id must be alphanumeric")
        return value 
    
    class Config: 
        arbitrary_types_allowed = True 