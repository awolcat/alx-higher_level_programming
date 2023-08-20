#!/usr/bin/python3
"""This script will connect to the named database
    and query state names passed as CommandLine arguments
"""
import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    Host = 'localhost'
    User = args[1]
    Pass = args[2]
    DB = args[3]
    name = args[4]

    if ';' not in name:
        query = """SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY id ASC""".format(name)
        db = MySQLdb.connect(host=Host, user=User, password=Pass, database=DB)
        cursor = db.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            print(result)
