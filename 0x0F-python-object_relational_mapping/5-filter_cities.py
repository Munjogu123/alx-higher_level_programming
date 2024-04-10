#!/usr/bin/python3
""" Performs SQL queries in python script """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """takes in the name of a state as an
    argument and lists all cities of that state """
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute(
        "SELECT cities.name \
        FROM cities \
        LEFT JOIN states \
        ON cities.state_id = states.id \
        WHERE states.name LIKE BINARY '%{}'".format(argv[4])
    )
    rows = cur.fetchall()

    print(", ".join(row[0] for row in rows))    
