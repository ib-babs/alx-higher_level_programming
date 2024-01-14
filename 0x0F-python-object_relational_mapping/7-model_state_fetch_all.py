#!/usr/bin/python3
"""ORM - Object Relational Mapping Application
Fetch all from state"""


def fetch_all_from_state(engine):
    """Fetch all states columns"""
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State.id, State.name).order_by(State.id).all()
    for id, name in res:
        print('{}: {}'.format(id, name))
    session.close()


if __name__ == "__main__":
    from model_state import (State, Base)
    from sqlalchemy.orm import (sessionmaker)
    from sqlalchemy import create_engine
    from sys import argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    fetch_all_from_state(engine=engine)
