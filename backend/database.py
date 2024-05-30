from sqlalchemy import create_engine, Column, String, Integer, Date, Time, Boolean
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///backend/db_todo.db", echo=True)
Base = declarative_base()

class Tbl_Todo(Base):
	__tablename__ = "tbl_todo"
	
	id = Column(Integer, primary_key=True)
	author = Column(String)
	todo = Column(String)
	date = Column(Date)
	time = Column(Time)
	isdone = Column(Boolean)

Base.metadata.create_all(engine)