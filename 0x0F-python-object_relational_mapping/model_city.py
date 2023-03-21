#!/usr/bin/python3
<<<<<<< HEAD

"""
    this module contains a Base and City class
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer


Base = declarative_base()


class City(Base):
    """
        City class inherits the Base class
        Attributes:
            id (int)
            name (string)
            state_id (string)
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
=======
'''
    Defines classes for tables
'''
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    '''
        Creates table for cities
    '''
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")
>>>>>>> b95bb6843f82300f1bcc5e44f6aff07f0f6e7031
