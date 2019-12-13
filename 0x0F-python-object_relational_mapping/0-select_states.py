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
    db = MySQLdb.connect(host='localhost', user='username',
                         passwd='password', db='database_name')
    # Getting a cursor in MySQL python
    # it gives the ability to have multiple separete working environments through
    # the same connection to the database
    cur = db.cursor()


























"""
grabs all results from the cities table and prints them in asc order
by states.id
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    uname = sys.argv[1]
    upass = sys.argv[2]
    dbname = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=uname,
                         passwd=upass, db=dbname)
    c = db.cursor()
    c.execute("""SELECT * from states ORDER BY states.id ASC""")

    line = c.fetchone()
    while (line):
        print(line)
        line = c.fetchone()
