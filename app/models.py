from sqlalchemy import Column, Integer, String
from .database import Base

class Revenue(Base):
    __tablename__ = "revenue"

    id = Column(Integer, primary_key=True)
    month = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
