## Declaring the database

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    year = Column(Integer)
    finished_lab = Column(Boolean)

    def __repr__(self):
    	return '<Student(primary_key =%s, name = %s, year = %s, finished_lab = %s)>' % (
        self.id, self.name, self.year, self.finished_lab)
    
engine = create_engine('sqlite:///lecture.db')

Base.metadata.create_all(engine)

