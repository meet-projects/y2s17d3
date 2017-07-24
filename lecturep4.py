## Querying the database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lecturep2 import Base, Student

engine = create_engine('sqlite:///lecture.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# ## Part 1: Make a query to find all Students in the table
def show_all_the_students():
  students = # QUERY GOES HERE

  for student in students:
    # ADD YOUR CODE HERE TO PRINT THE STUDENT VALUE


# ## Part 2: Deleting an entry
# ADD CODE HERE

# ## Part 3: Updating an entry
# ADD CODE HERE

show_all_the_students()