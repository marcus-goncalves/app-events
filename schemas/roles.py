from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Role(BaseModel):
    name: str
    is_active: bool = True

    class Config:
        from_attributes = True

class CreateRole(Role):
    pass

class UpdateRole(Role):
    name: Optional[str]
    is_active: Optional[bool]

class ResponseRole(Role):
    id: int
    created_at: datetime