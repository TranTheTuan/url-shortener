from operator import index
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from .database import Base

class URL(Base):
  __tablename__ = "urls"

  id = Column(Integer, primary_key=True)
  target_url = Column(String(255), index=True)
  key = Column(String(6), index=True, unique=True)
  clicks = Column(Integer, default=0)
  is_active = Column(Boolean, default=True)
  secret_key = Column(String(255), index=True, unique=True)