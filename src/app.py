# Eleventh commit to github
# Urgency and rushing again!!

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

class Ships(Base):
    __tablename__ = 'ships'
    id = Column(Integer, primary_key=True)
    ships_name = Column(String(250))
    ships_number = Column(String(250))    
    person = relationship(Person)

    def to_dict(self):
        return {}   

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planets_name = Column(String(250))
    planets_number = Column(String(250))    
    person = relationship(Person)

    def to_dict(self):
        return {}     

class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    films_name = Column(String(251))
    films_number = Column(String(251))    
    director = Column(String(251))
    productor = Column(String(251))

    def to_dict(self):
        return {} 

## Draw from SQLAlchemy base
render_er(Base, 'diagram_n5.png')