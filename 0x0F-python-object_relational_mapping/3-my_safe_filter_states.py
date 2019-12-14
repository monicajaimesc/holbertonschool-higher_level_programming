#!/usr/bin/python3
"""
SQL injection to delete all records of a table
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

    cur.execute("SELECT * FROM states WHERE name = %(state_searched)s """,
                {'state_searched': state_searched})
    rows = cur.fetchall()
    for row in rows:
        print(row)
