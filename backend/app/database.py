from fastapi import Request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///./app.db', connect_args={"check_same_thread": False})

Session = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

db_session = scoped_session(Session)

Base = declarative_base()
Base.query = db_session.query_property()


def get_db(request: Request):
    return request.state.db
