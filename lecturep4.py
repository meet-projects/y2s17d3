## Querying the database

from lecturep2 import Base, Student
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///lecture.db')
Base.metadata.bind = engine


DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# ## Part 1: Make a query to find all Students in the table
students = session.query(Student).all()
for student in students:
	print("primary key:", student.id, 
		"name:", student.name, "\n",
		"object:", student)
	