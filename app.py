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
            task = input("Enter your task: ")
            date = datetime.strptime(input("Enter your due date (YYYY-MM-DD): "), '%Y-%m-%d').date()
            
            user = Todo(name=name, todo=task, date=date)
            session.add(user)
            session.commit()
            
        case 2:
            print("Searching...")

        case 3:
            todo_id = int(input("Enter the ID of the todo item you want to update: "))
            new_name = input("Enter the updated name: ")
            new_task = input("Enter the updated task: ")
            new_date = datetime.strptime(input("Enter the updated due date (YYYY-MM-DD): "), '%Y-%m-%d').date()
            update_todo(todo_id, new_name, new_task, new_date)
            
        case 4:
            print("Exiting...")
                        
choice = input("[1] Add todo\n"
            "[2] View all todo list\n"
            "[3] Update todo\n"
            "[4] Exit\n"
            "Enter number of your choice: ")

menu(int(choice))