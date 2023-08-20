#!/usr/bin/python3
"""This module lists all states whose name starts with capital N
    in the database specified.
"""
import sys
import MySQLdb


if __name__ == '__main__':
    args = sys.argv
    User = args[1]
    Pass = args[2]
    Database = args[3]
    db = MySQLdb.connect(host="localhost", user=User, password=Pass,
                         database=Database)
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states
                   WHERE name LIKE BINARY 'N%'
                   ORDER BY id ASC""")
    states = cursor.fetchall()
    for state in states:
        print(state)
