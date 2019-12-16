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
    engine = create_engine('mysql+mysqldb://{:s}:{:s}@localhost:3306/{:s}'
                           .format(username, password, database_name))
    # METADATA passing in our Engine
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    # The above Session is associated with SQLite-enabled Engine
    # but it hasn’t opened any connections yet
    session = Session()
    # CREATE FIRST NEW query object which loads the first instance of the state
    first_object_query = session.query(State).order_by(State.id).first()
    if first_object_query:
        print("{}: {}".format(first_object_query.id, first_object_query.name))
    # If the table states is empty, print Nothing
    else:
        print("Nothing")
    session.close()
