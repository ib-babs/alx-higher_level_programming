#!/usr/bin/python3
"""
ORM - Object Relational Mapping Application
lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""


def relationship_state_city():
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        states = State
        Session = sessionmaker(bind=engine)
        session = Session()
        rows = session.query(states).join(
            City).order_by(states.id, City.id).all()
        for row in rows:
            print("{}: {}".format(row.id, row.name))
            for city in row.cities:
                print("    {}: {}".format(city.id, city.name))

        session.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    from relationship_city import City
    from relationship_state import State, Base
    from sqlalchemy.orm import (sessionmaker)
    from sqlalchemy import create_engine
    from sqlalchemy.engine.url import URL
    from sys import argv
    relationship_state_city()
