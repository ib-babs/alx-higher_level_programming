#!/usr/bin/python3
"""ORM - Object Relational Mapping Application
prints all City objects
from the database hbtn_0e_14_usa"""


def fetch_all_from_city():
    try:
        url = {'drivername': 'mysql+mysqldb',
               'username': argv[1],
               'password': argv[2],
               'host': '127.0.0.1',
               'port': 3306,
               'database': argv[3]
               }
        engine = create_engine(URL.create(**url))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        res = session.query(State.name, City.id, City.name).join(
            City, State.id == City.state_id).order_by(City.id)
        for state_name, city_id, city_name in res.all():
            print('{}: ({}) {}'.format(state_name, city_id, city_name))
        session.close()
    except Exception as e:
        pass


if __name__ == "__main__":
    from model_city import City
    from model_state import (State, Base)
    from sqlalchemy.orm import (sessionmaker,)
    from sqlalchemy import create_engine
    from sqlalchemy.engine.url import URL
    from sys import argv
    fetch_all_from_city()
