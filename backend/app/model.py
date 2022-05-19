from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserResponseBase(BaseModel):
    name: str
    email: EmailStr




class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime

    class Config:
        orm_mode = True
