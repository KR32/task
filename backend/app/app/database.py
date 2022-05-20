from fastapi import Request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from app import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, pool_size=30, max_overflow=120)

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
