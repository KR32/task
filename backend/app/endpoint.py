from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Union

from app.database import get_db
from app.crud import *
from app.model import *

router = APIRouter()


@router.get('/search', response_model=Union[List[UserResponse], int])
def get_all_users(
    name: Optional[str] = None,
    email: Optional[str] = None,
    skip: int = 0,
    limit: int = 10,
    fetch_row_count: Optional[bool] = None,
    all_rows: Optional[bool] = None,
    db_session: Session = Depends(get_db)
)-> Union[List[UserResponse], int]:
    """
    Get all users from the database with optional filters and pagination

    allowed query params:
    - name (str) case sensitive
    - email (str) case insensitive
    - skip (default: 0)
    - limit (default: 10)
    - fetch_row_count => if false then only return users, if true then return total rows count
    - all_rows => if true then return all rows, if false then return only rows with limit and skip (by default skip=0, limit=10)
    - order_by => order by field name with prefix '-' for descending order (by default ascending order)
    """

    return get_users(
        db_session=db_session,
        name=name,
        email=email,
        skip=skip,
        limit=limit,
        all_rows=all_rows,
        fetch_row_count=fetch_row_count
    )


@router.post('/create', response_model=UserResponse)
def register_user(
    user_data: UserResponseBase,
    db_session: Session = Depends(get_db)
):
    """
    Register a new user

    """
    return create_user(
        db_session=db_session,
        user_data=user_data
    )


@router.put('/update/user/{user_id}', response_model=UserResponse)
def update_user(
    user_id: int,
    user_date: UserResponseUpdate,
    db_session: Session = Depends(get_db)
):  
    """
    Update User by user_id
    """
    return update_user_by_id(
        user_id=user_id,
        user_data=user_date,
        db_session=db_session
    )


@router.delete('/delete/user/{user_id}', response_model=Union[str, UserResponse])
def delete_user(
    user_id: int,
    user_response: bool = False,
    db_session: Session = Depends(get_db)
):
    """
    Delete user by user_id

    **params:**

    * user_id: user_id
    * user_response: if True, return UserResponse instead of str
    * db_session: database session
    """
    return delete_user_by_id(
        user_id=user_id,
        db_session=db_session,
        send_user_response=user_response
    )
