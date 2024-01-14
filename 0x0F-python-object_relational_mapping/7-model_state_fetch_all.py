#!/usr/bin/python3
"""ORM - Object Relational Mapping Application
Fetch all from state"""


def fetch_all_from_state():
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
        res = session.query(State.id, State.name).order_by(State.id).all()
        session.close()

        for id, name in res:
            print('{}: {}'.format(id, name))
    except Exception as e:
        pass


if __name__ == "__main__":
    from model_state import (State, Base)
    from sqlalchemy.orm import (sessionmaker,)
    from sqlalchemy import create_engine
    from sqlalchemy.engine.url import URL
    from sys import argv
    fetch_all_from_state()
