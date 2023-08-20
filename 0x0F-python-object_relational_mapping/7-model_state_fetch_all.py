#!/usr/bin/python3
"""This module defines a script that extracts
    rows from the states table or State objects
"""
import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    args = sys.argv
    User = args[1]
    Pass = args[2]
    Host = 'localhost'
    DB = args[3]
    URL = 'mysql+mysqldb://{}:{}@{}/{}'.format(User, Pass, Host, DB)

    engine = create_engine(URL, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State.id, State.name).order_by(State.id).all()
    session.close()
    for result in results:
        print('{}: {}'.format(result[0], result[1]))
