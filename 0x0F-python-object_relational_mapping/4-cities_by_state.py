#!/usr/bin/python3
""" Performs SQL queries in python script """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ lists all cities from the database hbtn_0e_4_usa """
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name \
        FROM cities, states \
        WHERE states.id = cities.state_id")
    rows = cur.fetchall()

    for row in rows:
        print(row)
