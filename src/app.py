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

class Ships(Base):
    __tablename__ = 'ships'
    id = Column(Integer, primary_key=False)
    ships_name = Column(String(10), nullable=False)
    ships_number = Column(String(10), nullable=False)    

    # def to_dict(self):
    #     return {}    


## Draw from SQLAlchemy base
render_er(Base, 'diagram_n30.png')