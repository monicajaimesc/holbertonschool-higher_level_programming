#!/usr/bin/python3
"""
lists all states from hbtn_0e_0_usa data base
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # connection to the database to use
    # the parameters are passed to the Python extension _mysql.
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=database_name)
    # Getting a cursor in MySQL python
    # it gives the ability to have multiple separete working environments through
    # the same connection to the database
    cur = db.cursor()
    # the execution function requires 1 parameter, the query
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    # after execute any select statement, select one method
    rows = cur.fetchall()
    for row in rows:
        print(row)
