from datetime import datetime
from pydantic import BaseModel, EmailStr, conint


# user auth schema

class UserCreate(BaseModel):
    email:EmailStr
    password:str


class UserResponse(BaseModel):
    # avoid returning the password to the user
    user_id:int
    email:EmailStr
    created_at:datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    type:str
    class Config:
        orm_mode = True
    
class TokenPayLoad(BaseModel):
    user_id:int

