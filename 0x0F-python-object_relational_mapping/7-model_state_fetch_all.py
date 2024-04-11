#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    """ lists all State objects from the database hbtn_0e_6_usa """
    db_url = "mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3], pool_pre_ping=True)
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    for value in session.query(State).order_by(State.id):
        print(f'{value.id}: {value.name}')
