#!/usr/bin/python3
"""This module defines one script
    that queries the database specified
    in the CommandLine for all City objects
    exploiting the relationship with States
    to return the corresponding state names
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

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
    results = session.query(City.name, City.id, State.name).\
        join(State).all()

    for result in results:
        st = result[2]
        ct_id = result[1]
        ct_nm = result[0]
        print('{}: ({}) {}'.format(st, ct_id, ct_nm))
