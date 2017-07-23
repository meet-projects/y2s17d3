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

# students = session.query(Student).all()

# for student in students:
# 		print("PRIMARY_KEY:", student.id, "\n",
# 		"name:", student.name, "\n",
# 		"year:", student.year, "\n",
# 		"finished_lab:", student.finished_lab, "\n")


# ## Part 2: Deleting an entry

# delete_example = session.query(Student).\
# filter_by(name = "Best Student").one()

# session.delete(delete_example)

# session.commit()

# ## Part 3: Updating an entry

# update_example = session.query(Student).\
# filter_by(finished_lab = None).all()

# for example in update_example:
# 	example.year = 2	
# 	example.finished_lab = False

# session.commit()

