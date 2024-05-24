from sqlalchemy.orm import sessionmaker
from backend.database import Todo, engine
from datetime import datetime

def menu(choice):
    match choice:
        case 1:
            Session = sessionmaker(bind=engine)
            session = Session()
            
            name = input("Enter your name: ")
            todo = input("Enter your task: ")
            date = datetime.strptime(input("Enter your due date (YYYY-MM-DD): "), '%Y-%m-%d').date()
            # time = input("Enter your due time: ")
            
            user = Todo(name=name, todo=todo, date=date)
            session.add(user)
            session.commit()
            
            
        case 2:
            print("Searching...")
        case 3:
            print("Exiting...")
                        
choice = input("[1] Add todo\n"
            "[2] View all todo list\n"
            "[3] Search\n"
            "[4] Exit\n"
            "Enter number of your choice: ")

menu(int(choice))
    