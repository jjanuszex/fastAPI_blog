#in this file we define the database models

from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, text
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.sqltypes import TIMESTAMP


#jeśli chcemy zmienić atrybuty tabeli to musimy zmienić je w tym pliku,
# ale musimy uzyć narzedzia Alembic które pozwala na migracje bazy danych
# w tym przypdaku zrobimy drop table i create table
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)

