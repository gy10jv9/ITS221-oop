from sqlalchemy.orm import sessionmaker
from backend.database import Task, engine

def update_todo(todo_id, new_task, new_date):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    todo = session.query(Task).filter_by(id=id).one_or_none()
    
    if not todo:
        print("Todo item not found.")
    else:
        Task.todo = new_task
        Task.date = new_date
        
        session.commit()
        print("Todo item updated successfully!")