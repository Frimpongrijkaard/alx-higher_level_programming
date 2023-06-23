#!/usr/bin/python3
"""
A cript that alter the name of a State 
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    change a State object on the database.
    """

    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.id == '2').first()
    state.name = 'New Mexico'
    session.commit()
    session.close()
