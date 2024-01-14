#!/usr/bin/python3
"""ORM - Object Relational Mapping Application
Modelling State class"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sys import argv
from sqlalchemy.engine.url import URL

Base = declarative_base()
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    argv[1], argv[2], argv[3]), pool_pre_ping=True)


class State(Base):
    """Derived class of Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
