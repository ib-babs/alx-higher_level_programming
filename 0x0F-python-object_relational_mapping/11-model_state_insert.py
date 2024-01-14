#!/usr/bin/python3
"""ORM - Object Relational Mapping Application
Insert new data into `states` table"""


def insert_model():
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

        louisiana = State(name="Louisiana")
        Session = sessionmaker(bind=engine)

        session = Session()
        session.add(louisiana)
        res = session.query(State.id).first()
        print(louisiana.id)
        session.commit()
        session.close()
    except Exception as e:
        pass


if __name__ == "__main__":
    from model_state import (State, Base)
    from sqlalchemy.orm import (sessionmaker,)
    from sqlalchemy import create_engine
    from sqlalchemy.engine.url import URL
    from sys import argv
    insert_model()
