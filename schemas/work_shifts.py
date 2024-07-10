from pydantic import BaseModel, Field
from datetime import datetime

class WorkShift(BaseModel):
    description: str
    
    class Config:
        from_attributes = True

class CreateWorkShift(WorkShift):
    name_key: str
    pass

class ResponseWorkShift(WorkShift):
    id: int
    name_key: str
    created_at: datetime