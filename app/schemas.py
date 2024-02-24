from pydantic import BaseModel, EmailStr, validator, Field
import re
from typing import List, Optional


# showing to user these info
class UserDisplay(BaseModel):
    id: str
    firstname: str
    lastname: str
    username: str
    email: str
    mobile: str
    country: str
    model_config = {
        "from_attributes": True,
    }


# valdating user input to create info
class UserCreate(BaseModel):
    firstname: str = Field(..., min_length=1)
    lastname: str = Field(..., min_length=1)
    username: str = Field(..., min_length=1)
    email: EmailStr
    mobile: str = Field(..., min_length=10)
    country: str
    password: str = Field(..., min_length=6)


# valdating user inputs to get user info
class UserGet(BaseModel):
    id: Optional[str] = None
    email: Optional[EmailStr] = None
    username: Optional[str] = None


class User(BaseModel):
    email: str
    company: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class LoginDisplay(BaseModel):
    user: UserDisplay
    access_token: str
    token_type: str
