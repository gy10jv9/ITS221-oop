from backend.database import Task, Author
from datetime import datetime
from update import update_todo
from delete import delete_todo

def menu(choice):
    match choice:
        case 1:
            
            Author_Obj = Author()
            author_id = Author_Obj.add(input("Enter your name: "))
            
            task = {
                'author_id': author_id,
                'task': input("Enter your task: "),
                'date': datetime.strptime(input("Enter your due date (YYYY-MM-DD): "), '%Y-%m-%d').date(),
                'time': datetime.strptime(input("Enter your due time (HH:MM): "), '%H:%M').time(),
                'isdone': False
            }

            Task_Obj = Task()
            Task_Obj.add(task)
            
        case 2:
            Task_Obj.viewall()

        case 3: #update.py :P
            todo_id = int(input("Enter the ID of the todo item you want to update: "))
            new_todo = input("Enter the updated task: ")
            
            update_todo(todo_id, new_todo)
        
        case 4: #delete.py
            todo_id = int(input("Enter the ID of the todo item you want to delete: "))
            delete_todo(todo_id)
                 
        case 5:
            exit("Exiting...")

while True:
    print("[1] Add todo\n"
        "[2] View all todo list\n"
        "[3] Update todo\n"
        "[4] Exit\n") 
    choice = input("Enter number of your choice: ")

    menu(int(choice))

