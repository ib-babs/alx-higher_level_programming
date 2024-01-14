#!/usr/bin/python3
"""ORM - Object Relational Mapping Application
Delete data from `states` table"""


def delete_column_data(engine):
    """Delete column"""
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).filter(State.name.contains('a')).all()
    for row in res:
        session.delete(row)
    session.commit()
    session.close()


if __name__ == "__main__":
    from model_state import (State, Base)
    from sqlalchemy.orm import (sessionmaker)
    from sqlalchemy import create_engine
    from sys import argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    delete_column_data(engine=engine)
