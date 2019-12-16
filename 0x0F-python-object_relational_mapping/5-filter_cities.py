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

    cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id\
                = states.id WHERE states.name LIKE BINARY %s ORDER BY\
                cities.id;", (sys.argv[4], ))
    result = cur.fetchall()
    line = []
    for row in result:
        line.append(row[0])
    print(", ".join(line))
