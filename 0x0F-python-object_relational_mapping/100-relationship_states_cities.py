#!/usr/bin/python3
"""
ORM - Object Relational Mapping Application
creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa"""


def relationship_state_city(engine):
    """Create related data"""
    Base.metadata.create_all(engine)

    state = State(name="California", cities=[City(name="San Francisco")])
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    from relationship_state import (State, Base)
    from relationship_city import City
    from sqlalchemy.orm import (sessionmaker)
    from sqlalchemy import create_engine
    from sys import argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    relationship_state_city(engine=engine)
