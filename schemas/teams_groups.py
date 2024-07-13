from pydantic import BaseModel
from datetime import datetime

class TeamsGroup(BaseModel):
    group_name: str
    
    class Config:
        from_attributes = True

class CreateTeamsGroup(TeamsGroup):
    name_key: str

class ResponseTeamsGroup(TeamsGroup):
    id: int
    created_at: datetime