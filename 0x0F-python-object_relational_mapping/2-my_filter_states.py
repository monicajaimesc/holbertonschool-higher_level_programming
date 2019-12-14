#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_searched = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database_name)

    cur = db.cursor()
    # like or = is the same
    cur.execute("SELECT * FROM states "
                "WHERE name LIKE BINARY '{:s}'"
                "ORDER BY states.id ASC".format(state_searched))
    rows = cur.fetchall()
    for row in rows:
        print(row)
