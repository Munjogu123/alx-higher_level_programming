#!/usr/bin/python3
""" Uses sqlalchemy view objects in the database """
from model_state import Base, State
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    """ adds the State object “Louisiana” to the database """
    db_url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    print(state.id)
    session.close()
