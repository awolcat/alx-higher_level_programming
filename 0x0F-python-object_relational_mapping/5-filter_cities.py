#!/usr/bin/python3
"""This script will connect to the named database
    and query city names in the state passed as a CommandLine argument
"""
import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    Host = 'localhost'
    User = args[1]
    Pass = args[2]
    DB = args[3]
    state = args[4]

    if ';' not in state:
        query = """SELECT cities.name
                FROM cities LEFT JOIN states on cities.state_id = states.id
                WHERE states.name LIKE BINARY '{}'
                ORDER BY cities.id ASC""".format(state)

        db = MySQLdb.connect(host=Host, user=User, password=Pass, database=DB)
        cursor = db.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        results_list = []
        for result in results:
            results_list += result
        """for result in results:
        """
        print(', '.join(results_list))
