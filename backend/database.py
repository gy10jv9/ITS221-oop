from sqlalchemy import create_engine, Column, String, Integer, Date, Time, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///backend/db_todo.db", echo=False)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Task(Base):
	__tablename__ = "tbl_todo"
	
	id = Column(Integer, primary_key=True)
	author_id = Column(Integer, ForeignKey('tbl_authors.id'))
	task = Column(String)
	date = Column(Date)
	time = Column(Time)
	isdone = Column(Boolean)
 
	def add(self, payload):
		todo = Task(author_id=payload["author_id"], task=payload["task"], date=payload["date"], time=payload["time"], isdone=False)
		session.add(todo)
		session.commit()


class Author(Base):
	__tablename__ = "tbl_authors"
	
	id = Column(Integer, primary_key=True)
	author = Column(String)
 
	def add(self, payload):
		author = session.query(Author).filter_by(author=payload).first()
		if not author:
			author = Author(author=payload)
			session.add(author)
			session.commit()
   
		return author.id
	

Base.metadata.create_all(engine)