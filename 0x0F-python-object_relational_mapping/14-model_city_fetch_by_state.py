#!/usr/bin/python3
"""
uses sqlalchemy to list all state objects in given database
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{:s}:{:s}@localhost:3306/{:s}'
                           .format(username, password, database_name))

    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    for city, state in session.query(City, State).\
            filter(State.id == City.state_id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
