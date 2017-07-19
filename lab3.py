from sqlalchemy import create_engine
## Inserting into database
from sqlalchemy.orm import sessionmaker
 
from lab2 import Base, Student
engine = create_engine('sqlite:///intro.db')
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
 
# Insert a Student into the student table
student_1 = Student(name='Orhan')
session.add(student_1)
student_2 = Student(name='Helen')
session.add(student_2)
student_3 = Student(name='Avital')
session.add(student_3)
student_4 = Student(name='Matt')
session.add(student_4)
student_5 = Student(name='Bassil')
session.add(student_5)
session.commit()
 