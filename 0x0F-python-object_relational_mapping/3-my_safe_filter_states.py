#!/usr/bin/python3
""" Performs SQL queries in python script """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument"""
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s", (argv[4],))
    rows = cur.fetchall()

    for row in rows:
        print(row)
