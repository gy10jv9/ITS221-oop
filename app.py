from sqlalchemy.orm import sessionmaker
from backend.database import Todo, engine
from datetime import datetime
from update import update_todo

def menu(choice):
    match choice:
        case 1:
            Session = sessionmaker(bind=engine)
            session = Session()
            
            name = input("Enter your name: ")
            todo = input("Enter your task: ")
            date = datetime.strptime(input("Enter your due date (YYYY-MM-DD): "), '%Y-%m-%d').date()
            time = datetime.strptime(input("Enter your due time (HH:MM:SS): "), '%H:%M:%S').time()
            
            user = Todo(name=name, todo=todo, date=date, time=time, isdone=False)
            session.add(user)
            session.commit()
            
        case 2:
            Session = sessionmaker(bind=engine)
            session = Session()
            
            todos = session.query(Todo).all()
            for todo in todos:
                print(f"ID: {todo.id}")
                print(f"Name: {todo.name}")
                print(f"Task: {todo.todo}")
                print(f"Due Date: {todo.date}")
                print(f"Due Time: {todo.time}")
                print(f"Is Done: {todo.isdone}")
                print("--------------------")

        case 3: #update.py :P
            todo_id = int(input("Enter the ID of the todo item you want to update: "))
            new_todo = input("Enter the updated task: ")
            
            update_todo(todo_id, new_todo)
            
        case 4:
            exit("Exiting...")

while True:
    print("[1] Add todo\n"
        "[2] View all todo list\n"
        "[3] Update todo\n"
        "[4] Exit\n") 
    choice = input("Enter number of your choice: ")

    menu(int(choice))

