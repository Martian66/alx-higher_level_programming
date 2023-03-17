#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Access point to the database
    """

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

# cursor object
mycursor = db.cursor()
mycursor.execute("SELECT * FROM `states`")
results = mycursor.fetchall()

# print each state name
for state in results:
    print(state)
