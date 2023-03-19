#!/usr/bin/python3
""" This script uses ORM to define a City class and
a Base class that can be used to interact with a MySQL database """

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class
    Attributes:
    __tablename__(str): the name of table class
    id (int): The City's id
    name (str): the City's name of the class
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
