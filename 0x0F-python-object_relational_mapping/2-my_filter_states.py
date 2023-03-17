#!/usr/bin/python3
""" A script that lists all states from the database hbtn_0e_0_usa """


import MySQLdb
import sys

if __name__ == '__main__':
    """
     Access point to the database
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])

    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM states \
                     WHERE name LIKE BINARY '{}' \
                     ORDER BY states.id ASC".format(argv[4]))
    rows = mycursor.fetchall()

    for row in rows:
        print(row)
