#!/usr/bin/python3
"""
print all state objects in a database
with names that contain an a
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{:s}:{:s}@localhost:3306/{:s}'
                           .format(username, password, database_name))

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    for instance in session.query(State).filter(State.name.contains('a')):
        print("{}: {}".format(instance.id, instance.name))
