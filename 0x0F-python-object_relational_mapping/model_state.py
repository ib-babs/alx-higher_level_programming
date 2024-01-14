#!/usr/bin/python3
"""ORM - Object Relational Mapping Application
Modelling State class
State is the class consructing for the
rest of the program"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sys import argv

Base = declarative_base()


class State(Base):
    """Derived class of Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
    argv[1], argv[2], argv[3]), pool_pre_ping=True)
