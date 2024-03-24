#in this file we define the database models

from .database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True)