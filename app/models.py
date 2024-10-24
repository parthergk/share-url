from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String, unique=True, nullable=False)
    shared_items = relationship("SharedItem", back_populates="group")

class SharedItem(Base):
    __tablename__ = "shared_items"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, nullable=False)
    shared_at = Column(DateTime, default=datetime.utcnow)
    group_id = Column(Integer, ForeignKey("groups.id"))
    group = relationship("Group", back_populates="shared_items")
