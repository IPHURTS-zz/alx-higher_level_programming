#!/usr/bin/python3
<<<<<<< HEAD

"""
    this module contains a Base and State class
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer

=======
"""
class definition of a State and an instance Base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
>>>>>>> b95bb6843f82300f1bcc5e44f6aff07f0f6e7031

Base = declarative_base()


class State(Base):
    """
<<<<<<< HEAD
        State class inherits the Base class
        Attributes:
            id (int)
            name (string)
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
=======
    State class:
    inherits from Base
    links to the MySQL table states
    class attribute id that represents a column of an auto-generated,
    unique integer, cant be null and is a primary key
    class attribute name that represents a column of a string
    with maximum 128 characters and cant be null
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
>>>>>>> b95bb6843f82300f1bcc5e44f6aff07f0f6e7031
    name = Column(String(128), nullable=False)
