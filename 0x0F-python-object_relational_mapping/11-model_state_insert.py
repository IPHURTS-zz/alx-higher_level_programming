#!/usr/bin/python3
"""
<<<<<<< HEAD
    A script that adds the State object 'Louisiana' to hbtn_0e_6_usa
    Username, password, dbname will be passed as arguments to the script.
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

    # create the object and add it
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # print state.id
    state_add = session.query(State).filter(State.name == 'Louisiana').one()
    print(state_add.id)

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
    new_obj = State(name='Louisiana')
    session.add(new_obj)
    session.commit()
    print(new_obj.id)
>>>>>>> b95bb6843f82300f1bcc5e44f6aff07f0f6e7031
    session.close()
