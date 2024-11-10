from pydantic import BaseModel, Field, validator 
from typing import Optional 
from bson.objectid import ObjectID

class Project(BaseModel):
    _id: Optional[ObjectID] 
    project_id:  str = Field(..., min_length=1)
    
    @validator("project_id")
    def validate(cls, value):
        if not value.isalnum():
            raise ValueError("project_id must be alphanumeric")
        return value 
    
    class Config: 
        arbitrary_types_allowed = True 