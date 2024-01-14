#!/usr/bin/python3
"""ORM - Object Relational Mapping Application
Fetch rows that contain 'a' from state"""


def fetch_a_from_state(engine):
    """Fetch rows contain letter 'a'"""
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State.id, State.name).filter(
        State.name.contains("a"))
    for id, name in res.all():
        print('{}: {}'.format(id, name))
    session.close()


if __name__ == "__main__":
    from model_state import (State, Base)
    from sqlalchemy.orm import (sessionmaker)
    from sqlalchemy import create_engine
    from sys import argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    fetch_a_from_state(engine=engine)
