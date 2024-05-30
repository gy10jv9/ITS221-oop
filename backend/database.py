from sqlalchemy import create_engine, Column, String, Integer, Date, Time, Boolean, ForeignKey
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

class Tbl_Todo2(Base):
	__tablename__ = "tbl_todo2"
	
	id = Column(Integer, primary_key=True)
	author_id = Column(Integer, ForeignKey('tbl_authors.id'))
	task = Column(String)
	date = Column(Date)
	time = Column(Time)
	isdone = Column(Boolean)

class Tbl_Authors(Base):
	__tablename__ = "tbl_authors"
	
	id = Column(Integer, primary_key=True)
	author = Column(String)

Base.metadata.create_all(engine)