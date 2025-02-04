from pydantic import BaseModel
from datetime import datetime

class Schedule(BaseModel):
    description: str
    
    class Config:
        from_attributes = True

class CreateSchedule(Schedule):
    name_key: str

class ResponseSchedule(Schedule):
    id: int
    created_at: datetime