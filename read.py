#read
from sqlalchemy.orm import sessionmaker
from app import User, engine

Session = sessionmaker(bind=engine)
session = Session()

users = session.query(User).all()

for user in users:
    print(f"User ID: {user.ssn}, First Name: {user.firstname},  Last Name: {user.lastname}, Gender: {user.gender}, Age: {user.age}")
        print(f"User ID: {user.ssn}, First Name: {user.firstname},  Last Name: {user.lastname}, Gender: {user.gender}, Age: {user.age}")     