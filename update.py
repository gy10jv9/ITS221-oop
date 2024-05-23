#update
from sqlalchemy.orm import sessionmaker
from app import User, engine

Session = sessionmaker(bind=engine)
session = Session()

users = session.query(User).filter_by(ssn=2).one_or_none()

print(f"From: ", users.firstname)

users.firstname = "Gwen"
print(f"Changed to: ",users.firstname)

session.commit()