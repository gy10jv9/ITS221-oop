from sqlalchemy.orm import sessionmaker
from backend.database import Tbl_Todo, engine
from datetime import datetime
from update import update_todo
from classes.Task import Task

def menu(choice):
    Task_Obj = Task()
    
    match choice:
        case 1:
            task = {
                'author': input("Enter your name: "),
                'todo': input("Enter your task: "),
                'date': datetime.strptime(input("Enter your due date (YYYY-MM-DD): "), '%Y-%m-%d').date(),
                'time': datetime.strptime(input("Enter your due time (HH:MM): "), '%H:%M:%S').time(),
                'isdone': False
            }
            
            Task_Obj.add(task)
            
        case 2:
            Task_Obj.viewall()

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

