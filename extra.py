## Declaring the database

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# ## 1) Make an animal table with an id (PRIMARY KEY), and 3 columns:
# ## name, number_legs, cute.
# ## Name: String
# ## number_legs: Integer
# ## cute: Boolean



class Animal(Base):
    id = Column(Integer, primary_key=True)
    orhan = Column(String)
  # ADD CODE HERE


### Generate table
engine = create_engine('sqlite:///extra.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

# ## 2) Add 10 entries into this table.
# ADD CODE HERE


# ## 3) Query the table to find all the cute animals.
# ADD CODE HERE


# ## 4) Query the table to find all the animals with 4 legs.
# ADD CODE HERE


# ## 5) Query the table, and delete all animals that are NOT cute.
# ADD CODE HERE


# ## 6) Create a new table Mammal that inherit from Animal.
# If you don't know what it is look it up on google or ask a instructor

class Mammal(...):
  # ADD CODE HERE
