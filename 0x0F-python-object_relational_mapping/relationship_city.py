#!/usr/bin/python3
"""ORM - Object Relational Mapping Application
Modelling City class"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sys import argv


class City(Base):
    """Derived class of Base class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
