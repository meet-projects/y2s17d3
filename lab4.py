## Querying the database

from lab2 import Base, Student
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///lab2.db')
Base.metadata.bind = engine


DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# Make a query to find all Persons in the database
session.query(Student).all()
# Return the first Person from all Persons in the database
student = session.query(Student).first()
print(student.name)