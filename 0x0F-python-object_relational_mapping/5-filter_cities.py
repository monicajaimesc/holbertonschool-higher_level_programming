#!/usr/bin/python3
"""
Takes in the name of a state as an argument
and lists all cities of that state, using the database
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database_name)
    cur = db.cursor()

    cur.execute("SELECT c.name FROM cities AS c "
                "INNER JOIN states AS s ON c.state_id = s.id "
                "WHERE s.name = %(statename)s", {'statename': state_name})
    rows = cur.fetchall()
    for row in rows:
        print(", ".join(row))
