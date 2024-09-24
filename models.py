from sqlalchemy import Column,Integer,String,DateTime,func,UniqueConstraint
from database import Base

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,autoincrement=True)
    username=Column(String(50),unique=True,nullable=False)
    email=Column(String(100),unique=True,nullable=False)
    password=Column(String(200),unique=False,nullable=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now())

class Docs(Base):
    __tablename__='docs'
    id=Column(Integer,primary_key=True,autoincrement=True)
    filename=Column(String(100),unique=False,nullable=False)
    author=Column(String(50),unique=False,nullable=False)
    title=Column(String(100),unique=False,nullable=False)
    category=Column(String(100),unique=False,nullable=False)
    filepath=Column(String(100),unique=True,nullable=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    owner=Column(Integer,unique=False,nullable=False)
    __table_args__=(UniqueConstraint('owner','author','title','category'),)

class TimeProf(Base):
    __tablename__='timeprofile'
    id=Column(Integer,primary_key=True,autoincrement=True)
    session_id=Column(String(100),unique=False,nullable=False)
    user_id=Column(Integer,unique=False,nullable=False)
    api=Column(String(10),unique=False,nullable=False)
    start=Column(DateTime(timezone=True),nullable=False)
    end=Column(DateTime(timezone=True),nullable=False)