#!/usr/bin/python3
"""This script will delete all rows with 'a'
    in the name column of the named database
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
    DB = args[3]
    Host = 'localhost'

    URL = 'mysql+mysqldb://{}:{}@{}/{}'.format(User, Pass, Host, DB)

    engine = create_engine(URL, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).filter(State.name.like('%a%')).delete()
    session.commit()
    session.close()
