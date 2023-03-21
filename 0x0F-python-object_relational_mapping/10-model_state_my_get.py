#!/usr/bin/python3
<<<<<<< HEAD
"""
    A script that prints the State object with the name passed as an argument
    from hbtn_0e_6_usa
    Username, password, dbname and name to search
    will be passed as arguments to the script.
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
    states = session.query(State) \
                    .filter(State.name == sys.argv[4]).one_or_none()

    # print state.id
    if states is None:
        print("Not found")
    else:
        print(states.id)

=======
'''
a script that lists all State objects
from the database hbtn_0e_6_usa
'''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                        argv[2],
                                                        argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter_by(name=argv[4]).first()
    if state is not None:
            print(str(state.id))
    else:
        print("Not found")
>>>>>>> b95bb6843f82300f1bcc5e44f6aff07f0f6e7031
    session.close()
