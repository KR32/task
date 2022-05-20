from typing import List
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException

from app.db_model import User
from app.model import *

def get_user_by_email(
    email: str,
    db_session: Session
) -> User:
    email = email.lower()
    return db_session.query(User).filter(User.email == email).first()



def get_users(
    db_session: Session,
    user_id: Optional[int] = None,
    name: Optional[str] = None,
    email: Optional[str] = None,
    skip: int = None,
    limit: int = None,
    all_rows: bool = False,
    fetch_row_count: bool = False
) -> List[UserResponse]:

    query = db_session.query(User)

    if user_id:
        query = query.filter(User.user_id == user_id)

    if name:
        query = query.filter(User.name.contains(name))
    
    if email:
        query = query.filter(User.email == email)

    if not all_rows and (skip and limit):
        return query.offset(skip).limit(limit).all()

    if all_rows and fetch_row_count:
        return query.count()

    return query.all()



def create_user(
    db_session: Session,
    user_data: UserResponseBase
):
    user = db_session.query(User).filter_by(email=user_data.email).first()
    if user:
        raise HTTPException(status_code=400, detail='User already exists')
    user = User(**user_data.dict())
    return save(db_session=db_session, user=user)


def update_user_by_id(
    user_id: int,
    user_data: UserResponseUpdate,
    db_session: Session
) -> UserResponse:
    user = db_session.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    existing_user = jsonable_encoder(user)
    updated_user = jsonable_encoder(user_data)
    for field in existing_user:
        if field in updated_user:
            # check if any other user exist in db with this same updated email
            if field == 'email':
                if get_user_by_email(email=updated_user[field], db_session=db_session):
                    raise HTTPException(
                        status_code=400,
                        detail='User with email {} already exists'.format(updated_user[field])
                    )
            # endif
            setattr(user, field, updated_user[field])

    return save(db_session=db_session, user=user)


def delete_user_by_id(
    user_id: int,
    db_session: Session
):
    user = db_session.query(User).filter(User.user_id == user_id).scalar()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return save(db_session=db_session, user=user)


def save(db_session: Session, user: User):
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user
