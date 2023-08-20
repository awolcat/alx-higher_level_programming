#!/usr/bin/python3
import sys
import MySQLdb

"""This module lists all states in the database
    specified
"""


def show_states():
    """This function accesses the specified database through MySQLdb driver
        specifically accessing the states table and printing its contents
    """
    args = sys.argv
    User = args[1]
    Pass = args[2]
    Database = args[3]
    db = MySQLdb.connect(host="localhost", user=User, password=Pass,
                         database=Database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)


if __name__ == '__main__':
    show_states()
