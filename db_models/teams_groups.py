from sqlalchemy import Column, func
from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import relationship
from services.database import Base

class TeamsGroup(Base):
    __tablename__ = "teams_group"

    id = Column(Integer, primary_key=True)
    name_key = Column(String, nullable=False, unique=True)
    group_name = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    users = relationship("User", back_populates="teams_group")