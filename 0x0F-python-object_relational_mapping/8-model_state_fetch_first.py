#!/usr/bin/python3
"""ORM - Object Relational Mapping Application
Fetch from state"""


def fetch_first_from_state(engine):
    """Fetch first row"""
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State.id, State.name).first()
    if res:
        print('{}: {}'.format(res[0], res[1]))
    else:
        print("Nothing")
    session.close()


if __name__ == "__main__":
    from model_state import (State, Base)
    from sqlalchemy.orm import (sessionmaker)
    from sqlalchemy import create_engine
    from sys import argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    fetch_first_from_state(engine=engine)
