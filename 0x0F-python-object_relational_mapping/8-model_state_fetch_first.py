#!/usr/bin/python3
"""
uses sqlalchemy to prints the first State object from the database
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    # CONNECTION
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database_name))
    Session = sessionmaker()
    # The above Session is associated with SQLite-enabled Engine
    # but it hasn’t opened any connections yet
    session = Session(bind=engine)
    # CREATE FIRST NEW query object which loads the first instance of the state
    first_query = session.query(State).first()
    if first_query:
        print("{}: {}".format(first_query.id, first_query.name))
    # If the table states is empty, print Nothing
    else:
        print("Nothing")
