#!/usr/bin/python3
"""ORM - Object Relational Mapping Application
Delete data from `states` table"""


def delete_column_data():
    try:
        url = {'drivername': 'mysql+mysqldb',
               'username': argv[1],
               'password': argv[2],
               'host': '127.0.0.1',
               'port': 3306,
               'database': argv[3]
               }
        engine = create_engine(URL.create(**url))
        Session = sessionmaker(bind=engine)
        session = Session()
        res = session.query(State).filter(State.name.contains('a')).all()
        for row in res:
            session.delete(row)
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
    delete_column_data()
