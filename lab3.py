from sqlalchemy import create_engine
## Inserting into database
from sqlalchemy.orm import sessionmaker
 
from lab2 import Base, Student
engine = create_engine('sqlite:///lab2.db')
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
new_student = Student(name='Sample Student')
session.add(new_student)
session.commit()
 