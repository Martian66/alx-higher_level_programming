#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":

    mysql_user = sys.argv[1]
    mysql_pasword = sys.argv[2]
    database_name = sys.argv[3]

# establish database connection
mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=database_name
)

# cursor object
mycursor = mydb.cursor()

sql = "SELECT name FROM states ORDER BY id ASC"

# execute sql query
mycursor.execute(sql)

results = mycursor.fetchall()

# print each state name
for state in results:
    print(state[0])
