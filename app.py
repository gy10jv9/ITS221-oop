from backend.database import Task, Author
from datetime import datetime

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
            Task_Obj = Task()
            Task_Obj.viewall()

        case 3:
            todo_id = int(input("Enter the ID of the todo item you want to update: "))
            new_task = input("Enter the updated task: ")
            new_date = datetime.strptime(input("Enter the updated due date (YYYY-MM-DD): "), '%Y-%m-%d').date()
            new_time = datetime.strptime(input("Enter the updated due time (HH:MM): "), '%H:%M').time()
            isdone = input("Is the task done? (y/n): ").lower() == 'y'

            Task_Obj = Task()
            Task_Obj.update({
                'id': todo_id,
                'task': new_task,
                'date': new_date,
                'time': new_time,
                'isdone': isdone
            })
          
        case 4: #delete.py :P
            Task_Obj = Task()
            todo_id = int(input("Enter the ID of the todo item you want to delete: "))
            Task_Obj.delete(todo_id)  
            
        case 5: # para sa search
            print("[1] Search by task\n"
                "[2] Search by author\n"
                "[3] Search by date\n"
                "[4] Exit\n")
    
            choice = int(input("Enter number of your choice: "))
            Task_Obj = Task()
            
            match choice:
                case 1: 
                    task = input("Enter task to search: ")
                    Task_Obj.searchbyTask(task)
                case 2:
                    author = input("Enter author to search: ")
                    Task_Obj.searchbyAuthor(author)
                case 3:
                    date = datetime.strptime(input("Enter your due date (YYYY-MM-DD): "), '%Y-%m-%d').date()
                    Task_Obj.searchbyDate(date)
            
        case 6: # para sa search
            exit("Exiting...")

while True:
    print("[1] Add todo\n"
        "[2] View all todo list\n"
        "[3] Update todo\n"
        "[4} Delete todo\n"
        "[5} Search\n"
        "[6] Exit\n")
     
    choice = input("Enter number of your choice: ")

    menu(int(choice))