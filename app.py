from sqlalchemy.orm import sessionmaker
from backend.database import Todo, engine

def menu(choice):
    match choice:
        case 1:
            print("You selected option 1")
        case 2:
            print("Searching...")
        case 3:
            print("Exiting...")
                        
choice = input("[1] Add todo\n"
            "[2] View all todo list\n"
            "[3] Search\n"
            "[4] Exit\n"
            "[system] Enter number of your choice: ")

menu(int(choice))
    