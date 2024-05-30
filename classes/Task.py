from sqlalchemy.orm import sessionmaker
from backend.database import Tbl_Todo, Tbl_Authors, Tbl_Todo2, engine

Session = sessionmaker(bind=engine)
session = Session()

class Task:
    def add(self, payload):
        author = session.query(Tbl_Authors).filter_by(author=payload["author"]).first()
        if not author:
            author = Tbl_Authors(author=payload["author"])
            session.add(author)
            session.commit()

        todo = Tbl_Todo2(author_id=author.id, task=payload["task"], date=payload["date"], time=payload["time"], isdone=False)
        session.add(todo)
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