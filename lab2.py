## Inheritance

from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Building(Base):
    __tablename__ = 'building'
    id = Column(Integer, primary_key=True)
    building_type = Column(String(32), nullable=False)
    rent = Column(Float, nullable=False)
    __mapper_args__ = {'polymorphic_on': building_type}

    def __repr__(self):
        return '<Building(type = %r, rent = %r)>' %\
         (self.building_type, self.rent)

class Commercial(Building):
    __mapper_args__ = {'polymorphic_identity': 'commercial'}
    business = Column(String(50))

    def __repr__(self):
        return '<Commercial(business = %r, rent = %r)>' %\
         (self.business, self.rent)

class Residential(Building):
    __mapper_args__ = {'polymorphic_identity': 'residential'}
    num_residents = Column(Integer)

    def __repr__(self):
        return '<Residential(number of residents = %r, rent = %r)>' %\
         (self.num_residents, self.rent)


engine = create_engine('sqlite:///inherit.db')

Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)

session = DBSession()

commercial_building = Commercial(rent = 5000, 
    business = "bassil's business")
residential_building = Residential(rent = 2000,
    num_residents = 5)

session.add(commercial_building)
session.add(residential_building)
session.commit()

building_query = session.query(Building).all()
print(building_query)
commercial_query = session.query(Commercial).all()
print(commercial_query)
residential_query = session.query(Residential).all()
print(residential_query)
