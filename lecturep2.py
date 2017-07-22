## Declaring the database

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
    	return '<Student(name = %r)>' %\
    	 (self.name)
    
engine = create_engine('sqlite:///lecture.db')

Base.metadata.create_all(engine)

