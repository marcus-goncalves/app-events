from sqlalchemy import Column, func
from sqlalchemy import String, Integer, Boolean, DateTime
from sqlalchemy.orm import relationship
from services.database import Base

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=1)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    users = relationship("User", back_populates="role")