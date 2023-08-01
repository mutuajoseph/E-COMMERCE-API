from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserCreate):
    pass


class UserOut(UserBase):
    # public_id: str
    is_active: bool
    created: Optional[datetime]
    updated: Optional[datetime]

    class Config:
        orm_mode = True


class Login(UserBase):
    access_token: str
    token_type: str
    expires_in: Optional[Any]
    # user: Optional[UserOut]