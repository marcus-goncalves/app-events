from pydantic import BaseModel
from datetime import datetime

class WorkShift(BaseModel):
    description: str
    
    class Config:
        from_attributes = True

class CreateWorkShift(WorkShift):
    name_key: str

class ResponseWorkShift(WorkShift):
    id: int
    created_at: datetime