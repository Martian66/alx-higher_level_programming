#!/usr/bin/python3
""" This script uses ORM to define a state class and
a Base class that can be used to interact with a MySQL database """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):

    __tablename__ = 'states'

    id = Column(integer, primary_key=True)
    name = Column(string(128), nullable=False)
