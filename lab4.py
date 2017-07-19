## Querying the database

from lab2 import Base, Student
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///intro.db')
Base.metadata.bind = engine


DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# Make a query to find all Students in the database
students = session.query(Student).all()
for student in students:
	print("primary key:", student.id, 
		"name:", student.name, "\n",
		"object:", student)
