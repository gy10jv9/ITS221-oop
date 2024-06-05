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
  
	def viewall(self):
		tasks = session.query(Task).all()
		for task in tasks:
			print(f"ID: {task.id}\nAuthor ID: {task.author_id}\nTask: {task.task}\nDate: {task.date}\nTime: {task.time}\nIs Done: {task.isdone}\n")

	def delete(self, task_id):
		task = session.query(Task).filter_by(id=task_id).first()
		if task:
			session.delete(task)
			session.commit()
			print(f"Task with ID {task_id} has been deleted.")
		else:
			print(f"Task with ID {task_id} not found") 
            
	def searchbyTask(self, search_term):
		tasks = session.query(Task).filter(Task.task.contains(search_term)).all()
		for task in tasks:
			print(f"ID: {task.id}\nAuthor ID: {task.author_id}\nTask: {task.task}\nDate: {task.date}\nTime: {task.time}\nIs Done: {task.isdone}\n")
    
	def searchbyAuthor(self, author_id):
		tasks = session.query(Task).filter(Task.author_id == author_id).all()
		for task in tasks:
			print(f"ID: {task.id}\nAuthor ID: {task.author_id}\nTask: {task.task}\nDate: {task.date}\nTime: {task.time}\nIs Done: {task.isdone}\n")

	def searchbyDate(self, search_date):
		tasks = session.query(Task).filter(Task.date == search_date).all() 
		for task in tasks:
			print(f"ID: {task.id}\nAuthor ID: {task.author_id}\nTask: {task.task}\nDate: {task.date}\nTime: {task.time}\nIs Done: {task.isdone}\n")


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