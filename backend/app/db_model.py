from app.database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'

    user_id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(), nullable=False)
    email=Column(String(), nullable=False)
    