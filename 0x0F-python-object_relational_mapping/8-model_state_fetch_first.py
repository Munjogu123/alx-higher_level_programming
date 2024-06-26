#!/usr/bin/python3
""" Uses sqlalchemy view objects in the database """
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    """ prints the first State object from the database hbtn_0e_6_usa """
    db_url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    value = session.query(State).order_by(State.id).first()
    if value is not None:
        print(f'{value.id}: {value.name}')
    else:
        print("Nothing")
