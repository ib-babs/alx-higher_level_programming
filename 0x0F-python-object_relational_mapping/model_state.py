#!/usr/bin/python3
"""ORM - Object Relational Mapping Application
Modelling State class"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sys import argv
from sqlalchemy.engine.url import URL

Base = declarative_base()
url = {'drivername': 'mysql+mysqldb',
       'username': argv[1],
       'password': argv[2],
       'host': '127.0.0.1',
       'port': 3306,
       'database': argv[3]
       }
engine = create_engine(URL.create(**url))


class State(Base):
    """Derived class of Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
