from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from lecturep2 import Base, Student
engine = create_engine('sqlite:///lecture.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
 

# ## Part 1: Add a Student into the student table
student_1 = Student(name='Best Student')
session.add(student_1)
# session.commit()

# ## Part 1: Add the students in your group to the student table.
# ## relevant commands: add(STUDENT_INSTANCE)
# ## STUDENT_INSTANCE = Student(WHAT GOES IN HERE?)
# ## HINT: Don't forget to commit after you've added the 4 students.

group = {"Avital": True, "Helen": True, "Orhan": False, "Bassil": False, "Matt": True}

for student in group:
	session.add(Student(name = student, year = 2, finished_lab = group[student]))

session.commit() 

