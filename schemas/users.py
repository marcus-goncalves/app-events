from pydantic import BaseModel, EmailStr
from typing import Optional

class CreateUser(BaseModel):
    name: str
    password: str
    email: EmailStr

class UpdateUser(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    id_role: Optional[int]
    id_work_shift: Optional[int]
    id_schedule: Optional[int]
    is_active: Optional[bool]
