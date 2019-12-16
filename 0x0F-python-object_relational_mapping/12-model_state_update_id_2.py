#!/usr/bin/python3
"""
updates the name of a state object in the database
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
    update_state = session.query(State).filter(State.id == 2).all()
    if update_state:
        update_state[0].name = "New Mexico"
        session.commit()
        session.close()
