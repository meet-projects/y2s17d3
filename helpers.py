from lecturep2 import Base, Student
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def display_students():
  """ Display the students in the database """
  students = session.query(Student).all()

  for student in students:
      print(student)