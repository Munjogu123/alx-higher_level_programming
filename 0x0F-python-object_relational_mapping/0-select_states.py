#!/usr/bin/python3
""" This module connects MySQLdb to Python Script """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ executes SQL command from python script """
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)
