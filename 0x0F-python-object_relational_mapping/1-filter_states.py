#!/usr/bin/python3
"""
lists all states with a name starting with N from hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                "ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
