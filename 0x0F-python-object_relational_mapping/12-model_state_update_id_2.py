#!/usr/bin/python3
""" Uses sqlalchemy view objects in the database """
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    """ changes the name of a State object from the database  """
    db_url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    value = session.query(State).filter(State.id == 2).\
        update({State.name: "New Mexico"})

    session.commit()
    session.close()
