# Committing to github
# Urgency and rushing again !!

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=False)
    name = Column(String(10), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=False)
    street_name = Column(String(10))
    street_number = Column(String(10))
    post_code = Column(String(10), nullable=False)
    person = relationship(Person)

    # def to_dict(self):
    #     return {}

class Ships(Base):
    __tablename__ = 'ships'
    id = Column(Integer, primary_key=False)
    ships_name = Column(String(10), nullable=False)
    ships_number = Column(String(10), nullable=False)    

    # def to_dict(self):
    #     return {}      

class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    films_name = Column(String(10))
    films_number = Column(String(10))    
    director = Column(String(10))
    productor = Column(String(10))

    # def to_dict(self):
    #     return {} 

## Draw from SQLAlchemy base
render_er(Base, 'diagram_n24.png')