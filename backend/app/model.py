from typing import Optional
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, constr, validator, EmailStr

class UserResponseBase(BaseModel):
    name: constr(strip_whitespace=True)
    email: EmailStr

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
    email: Optional[EmailStr] = None
