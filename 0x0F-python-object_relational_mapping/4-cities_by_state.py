#!/usr/bin/python3
"""
lists all cities from the database
"""
from machine.programs.objects.AirBnB_clone_v3.api.v1.views import states

if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database_name)
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN\
                states ON cities.state_id = states.id ORDER BY cities.id;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

