from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from schemas import roles, schedules, work_shifts, teams_groups

class User(BaseModel):
    name: str
    email: EmailStr
    is_active: bool
    class Config:
        from_attributes = True


class CreateUser(User):
    password: str
    id_role: int
    id_work_shift: Optional[int]
    id_schedule: Optional[int]
    id_teams_group: Optional[int]

class UpdateUser(User):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    id_role: Optional[int] = None
    id_work_shift: Optional[int] = None
    id_schedule: Optional[int] = None
    id_teams_group: Optional[int] = None
    is_active: Optional[bool] = None

class ResponseUser(User):
    id: int
    role: roles.Role
    schedule: schedules.Schedule
    work_shift: work_shifts.WorkShift
    teams_group: teams_groups.TeamsGroup
    created_at: datetime
    updated_at: datetime | None