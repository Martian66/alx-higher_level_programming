#!/usr/bin/python3
""" This script uses ORM to define a state class and
a Base class that can be used to interact with a MySQL database """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class

    Attributes:
    __tablename__(str): the name of table class
    id (int): The state's id
    name (str): the state name of the class

    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
