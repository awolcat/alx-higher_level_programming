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

    query = """SELECT cities.id, cities.name, states.name
            FROM cities LEFT JOIN states ON states.id = cities.state_id
            ORDER BY id ASC"""
    db = MySQLdb.connect(host=Host, user=User, password=Pass, database=DB)
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        print(result)
