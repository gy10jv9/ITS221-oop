from sqlalchemy.orm import sessionmaker
from backend.database import Todo, engine
from datetime import datetime
from update import update_todo
from classes.Task import Task

def menu(choice):
    match choice:
        case 1:
            task = {
                'name': input("Enter your name: "),
                'todo': input("Enter your task: "),
                'date': datetime.strptime(input("Enter your due date (YYYY-MM-DD): "), '%Y-%m-%d').date(),
                'time': datetime.strptime(input("Enter your due time (HH:MM:SS): "), '%H:%M:%S').time(),
                'isdone': False
            }
            
            Task_Obj = Task()
            Task_Obj.add(task)
            
            
        case 2:
            Session = sessionmaker(bind=engine)
            session = Session()
            
            todos = session.query(Todo).all()
            for todo in todos:
                print(f"ID: {todo.id}"
                    f"Name: {todo.name}"
                    f"Task: {todo.todo}"
                    f"Due Date: {todo.date}"
                    f"Due Time: {todo.time}"
                    f"Is Done: {todo.isdone}"
                    "--------------------")

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

