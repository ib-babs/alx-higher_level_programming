#!/usr/bin/python3
"""ORM - Object Relational Mapping Application
prints the State object with the name passed as
argument from the database hbtn_0e_6_usa"""


def get_id(engine):
    """Get row by id"""
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State.id).filter(
        State.name == argv[4]).scalar()
    if (not res):
        print("Not found")
    else:
        print(res)
    session.close()


if __name__ == "__main__":
    from model_state import (State, Base)
    from sqlalchemy.orm import (sessionmaker)
    from sqlalchemy import create_engine
    from sys import argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    get_id(engine=engine)
