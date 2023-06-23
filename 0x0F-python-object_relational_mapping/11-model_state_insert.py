#!/usr/bin/python3
"""
A script that add  State 
`Louisiana` to the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Accessing state
    from the database.
    """

    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = State(name='Louisiana')
    session.add(state)
    session.commit()
    print('{0}'.format(state.id))
    session.close()
