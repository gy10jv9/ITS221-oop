from sqlalchemy.orm import sessionmaker
from backend.database import Todo, engine

Session = sessionmaker(bind=engine)
session = Session()

class Task:
    def add(self, payload):
        task = Todo(name=payload["name"], todo=payload["todo"], date=payload["date"], time=payload["time"], isdone=False)
        session.add(task)
        session.commit()