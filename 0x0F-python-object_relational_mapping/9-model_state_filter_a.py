#!/usr/bin/python3
"""
<<<<<<< HEAD
    A script that lists all State objects from hbtn_0e_6_usa that conatin
    the letter a from teh database.
    Username, password and dbname wil be passed as arguments to the script.
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    # create a session
    session = Session()

    # extract first state
    states = session.query(State).filter(State.name.ilike('%a%')) \
                    .order_by(State.id).all()

    # print states
    for state in states:
        print("{}: {}".format(state.id, state.name))

=======
All states via SQLAlchemy
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    data = session.query(State).order_by(State.id)\
                               .filter(State.name.like("%a%")).all()
    for row in data:
        print("{}: {}".format(row.id, row.name))
>>>>>>> b95bb6843f82300f1bcc5e44f6aff07f0f6e7031
    session.close()
