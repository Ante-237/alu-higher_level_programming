#!/usr/bin/python3
""" module gets all states """

if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    # create engine that binds to local port sql
    engine = create_engine('mysql+mysldb://{}:{}@localhost/{}'.
    format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # create session to interact with engine and run queries
    # handle engine creation from base
    Base.metadata.create_all(engine)
    session = Sessionmaker(bind=engine)

    lst = session.query(State).order_by(State.id)
    for i in lst:
        print("{}: {}".format(i.id, i.name))
