#!/usr/bin/python3
"""
ORM - Object Relational Mapping Application
creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa"""


def relationship_state_city():
    try:
        url = {'drivername': 'mysql+mysqldb',
               'username': argv[1],
               'password': argv[2],
               'host': '127.0.0.1',
               'port': 3306,
               'database': argv[3]
               }
        engine = create_engine(URL.create(**url))
        state = State(name="California", cities=[City(name="San Francisco")])
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(state)
        session.commit()
        session.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    from relationship_city import City
    from relationship_state import State
    from sqlalchemy.orm import (sessionmaker,)
    from sqlalchemy import create_engine
    from sqlalchemy.engine.url import URL
    from sys import argv
    relationship_state_city()
