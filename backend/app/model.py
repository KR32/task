from typing import Optional
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, constr, validator

EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class UserResponseBase(BaseModel):
    name: constr(strip_whitespace=True)
    email: constr(strip_whitespace=True, regex=EMAIL_REGEX)

    class Config:
        orm_mode = True

    @validator('name')
    def name_must_contain_character(cls, v):
        if v == "":
            raise HTTPException(
                status_code=400, 
                detail='Name must contain at least one character'
            )
        return v.title()



class UserResponse(UserResponseBase):
    user_id: int

class UserResponseUpdate(BaseModel):
    name: Optional[constr(strip_whitespace=True)] = None
    email: Optional[str] = None
