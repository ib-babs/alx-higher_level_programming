#!/usr/bin/python3
"""ORM - Object Relational Mapping Application
prints all City objects
from the database hbtn_0e_14_usa"""


def fetch_all_from_city(engine):
    """Print all city object"""
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State.name, City.id, City.name).join(
        City, State.id == City.state_id).order_by(City.id)
    for state_name, city_id, city_name in res.all():
        print('{}: ({}) {}'.format(state_name, city_id, city_name))
    session.close()


if __name__ == "__main__":
    from model_state import (State, Base)
    from model_city import City
    from sqlalchemy.orm import (sessionmaker)
    from sqlalchemy import create_engine
    from sys import argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    fetch_all_from_city(engine=engine)
