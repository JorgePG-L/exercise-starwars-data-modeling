import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class Usuario(Base):
    __tablename__ = 'usuario'
    id=Column(Integer, primary_key=True)
    Username=Column(String(250), nullable=False)
    Email = Column(String(120), nullable=False)
    Name = Column(String(120), nullable=False)
    Surname = Column(String(120), nullable=True)
    
class Planet(Base):
    __tablename__ = 'planet'
    id=Column(Integer, primary_key=True)
    name=Column(String(120), nullable=False)
    population=Column(Integer, nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id=Column(Integer, primary_key=True)
    name=Column(String(120), nullable=False)
    homeworld=Column(Integer, ForeignKey('planet.id'))
    home= relationship(Planet)
class Favourites(Base):
    __tablename__ = 'favourites'
    id= Column(Integer, primary_key=True)
    planet_id=Column(Integer, ForeignKey('planet.id'))
    planet= relationship(Planet)
    character_id=Column(Integer, ForeignKey('character.id'))
    character= relationship(Planet)
    usuario_id=Column(Integer, ForeignKey('usuario.id'))
    usuario= relationship(Planet)

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)


# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

