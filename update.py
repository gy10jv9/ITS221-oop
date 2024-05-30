from sqlalchemy.orm import sessionmaker
from backend.database import Task, engine

def update_todo(todo_id, new_todo):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    todo = session.query(Task).filter_by(id=todo_id).one_or_none()
    
    if not todo:
        print("Todo item not found.")
    else:
        todo.todo = new_todo
        
        session.commit()
        print("Todo item updated successfully!")