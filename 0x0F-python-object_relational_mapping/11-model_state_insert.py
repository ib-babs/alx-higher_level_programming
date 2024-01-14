#!/usr/bin/python3
"""ORM - Object Relational Mapping Application
Insert new data into `states` table"""


def insert_model(engine):
    """Insert into table"""
    Base.metadata.create_all(engine)

    louisiana = State(name="Louisiana")
    Session = sessionmaker(bind=engine)

    session = Session()
    session.add(louisiana)
    res = session.query(State.id).first()
    print(louisiana.id)
    session.commit()
    session.close()


if __name__ == "__main__":
    from model_state import (State, Base)
    from sqlalchemy.orm import (sessionmaker)
    from sqlalchemy import create_engine
    from sys import argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    insert_model(engine=engine)
