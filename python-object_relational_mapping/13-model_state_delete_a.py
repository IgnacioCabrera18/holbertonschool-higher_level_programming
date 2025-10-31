#!/usr/bin/python3
"""Lists all State objects from the database using SQLAlchemy ORM"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:'
        '{}@localhost/{}'.format(username, password, db_name),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    session = Session(engine)

    session.query(State).filter(State.name.like('%a%')).delete(synchronize_session=False)
    session.commit()

    session.close()
