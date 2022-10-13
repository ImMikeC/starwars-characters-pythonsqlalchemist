# 20th commit to github
# Urgency and rushing again!!

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Model = declarative_base()

class Ships(Model):
    __tablename__ = 'ships'
    id = Column(Integer, primary_key=True)
    ships_name = Column(String(250))
    ships_number = Column(String(250))    

    def to_dict(self):
        return {}   

class Planets(Model):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planets_name = Column(String(251))
    planets_number = Column(String(251))    

    def to_dict(self):
        return {}     

class Films(Model):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    films_name = Column(String(251))
    films_number = Column(String(251))    
    director = Column(String(251))
    productor = Column(String(251))

    def to_dict(self):
        return {} 

## Draw from SQLAlchemy base
render_er(Model, 'diagram_n5.png')