#!/usr/bin/python3
""" Uses sqlalchemy to perform SQL queries """
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    """ prints all City objects from the database hbtn_0e_14_usa """
    db_url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City).\
            join(City, State.id == City.state_id):

        print(f'{state.name}: ({city.id}) {city.name}')
