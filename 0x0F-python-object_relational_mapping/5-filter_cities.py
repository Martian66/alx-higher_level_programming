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
    mycursor.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': sys.argv[4]
        })

    rows = mycursor.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))
