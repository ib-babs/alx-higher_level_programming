#!/usr/bin/python3
"""ORM - Object Relational Mapping Application
Update data in `states` table"""


def update_column_data(engine):
    """Update column"""
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).filter_by(id=2).first()
    res.name = "New Mexico"
    session.commit()
    session.close()


if __name__ == "__main__":
    from model_state import (State, Base)
    from sqlalchemy.orm import (sessionmaker)
    from sqlalchemy import create_engine
    from sys import argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    update_column_data(engine=engine)
