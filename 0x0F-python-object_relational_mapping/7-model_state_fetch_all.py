#!/usr/bin/python3
"""
sqlalchemy to list all state objects in given database
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    # engine provides information about the database that is connecting to
    # create_engine is an instance of Engine,
    # handle details of the database and DBAPI
    # Python Database API specification
    # mysql+.. refers to the MySQL for Python
    engine = create_engine('mysql+mysqldb://@localhost/'.format
                           (username, password, database_name))

    # The table object member of a Metadata
    # the object is available using .metadata
    # attribute of the declarative base class
    # MetaData.create_all() method, passing in our Engine
    # as a source of database connectivity.
    Base.metadata.create_all(engine)
    # Ready to start talking to the database
    # Session class which will serve as a factory for new Session objects
    Session = sessionmaker()
    # connect engine with the session using configure()
    Session.configure(bind=engine)
    # conversation with the database, instantiate a session:
    session = Session()
    # new query object which loads instances of State order by id
    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))
