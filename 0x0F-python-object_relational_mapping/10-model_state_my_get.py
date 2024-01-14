#!/usr/bin/python3
"""ORM - Object Relational Mapping Application
Fetch rows that contain 'a' from state"""


def get_id():
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
        res = session.query(State.id).filter(
            State.name == argv[4]).scalar()
        if (not res):
            print("Not found")
        else:
            print(res)
        session.close()
    except Exception as e:
        pass


if __name__ == "__main__":
    from model_state import (State, Base)
    from sqlalchemy.orm import (sessionmaker,)
    from sqlalchemy import create_engine
    from sqlalchemy.engine.url import URL
    from sys import argv
    get_id()
