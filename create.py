#create data
from sqlalchemy.orm import sessionmaker
from app import User, engine

Session = sessionmaker(bind=engine)
session = Session()

user = User(firstname="Vincent", lastname="Manalo", gender='m', age=200)
user2 = User(firstname="Ben", lastname="Ten", gender='f', age=10)

session.add(user)
session.add(user2)
session.commit()