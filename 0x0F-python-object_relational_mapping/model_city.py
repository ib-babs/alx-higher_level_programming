#!/usr/bin/python3
"""ORM - Object Relational Mapping Application
Modelling City class"""
from model_state import Base
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sys import argv
from sqlalchemy.engine.url import URL

try:
    url = {'drivername': 'mysql+mysqldb',
           'username': argv[1],
           'password': argv[2],
           'host': '127.0.0.1',
           'port': 3306,
           'database': argv[3]
           }
    engine = create_engine(URL.create(**url))

    class City(Base):
        """Derived class of Base class"""
        __tablename__ = 'cities'
        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
        state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    Base.metadata.create_all(engine)


except Exception as e:
    pass
