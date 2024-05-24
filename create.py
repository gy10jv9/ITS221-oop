#create data
from sqlalchemy.orm import sessionmaker
from backend.database import Todo, engine

Session = sessionmaker(bind=engine)
session = Session()

user = Todo(name="Vincent")
# user2 = User(firstname="Ben", lastname="Ten", gender='f', age=10)

session.add(user)
# session.add(user2)
session.commit()