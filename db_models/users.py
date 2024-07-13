from sqlalchemy import Column, ForeignKey, func
from sqlalchemy import String, Integer, Boolean, DateTime
from sqlalchemy.orm import relationship
from services.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, nullable=False, default=1)
    id_role = Column(Integer, ForeignKey("roles.id"), nullable=False)
    id_schedule = Column(ForeignKey("schedules.id"), nullable=True)
    id_work_shift = Column(ForeignKey("work_shifts.id"), nullable=True)
    id_teams_group = Column(ForeignKey("teams_group.id"), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    role = relationship("Role", back_populates="users")
    schedule = relationship("Schedule", back_populates="users")
    work_shift = relationship("WorkShift", back_populates="users")
    teams_group = relationship("TeamsGroup", back_populates="users")