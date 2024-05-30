from sqlalchemy.orm import sessionmaker
from backend.database import Tbl_Todo, engine

Session = sessionmaker(bind=engine)
session = Session()

class Task:
    def add(self, payload):
        task = Tbl_Todo(author=payload["author"], todo=payload["todo"], date=payload["date"], time=payload["time"], isdone=False)
        session.add(task)
        session.commit()
        
    def viewall(self):
            todos = session.query(Tbl_Todo).all()
            for todo in todos:
                print(f"ID: {todo.id}\n"
                    f"Author: {todo.author}\n"
                    f"Task: {todo.todo}\n"
                    f"Due Date: {todo.date}\n"
                    f"Due Time: {todo.time}\n"
                    f"Is Done: {todo.isdone}\n"
                    "--------------------")