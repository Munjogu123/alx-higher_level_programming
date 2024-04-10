#!/usr/bin/python3
""" Performs SQL queries in python script """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ Lists all states starting with N """
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE(upper(name) LIKE 'N%')")
    rows = cur.fetchall()

    for row in rows:
        print(row)
