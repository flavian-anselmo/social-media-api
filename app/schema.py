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


# schema REQ
class PostBase(BaseModel): 
    title:str 
    description:str 
    published: bool = True 



class PostCreate(PostBase):
    pass 



class PostResponse(PostBase):
    postid:int 
    owner_id: int 
    owner: UserResponse # with user details 
    created_at: datetime

    # allow dict responses to be accepted
    class Config:
        orm_mode = True




class Token(BaseModel):
    access_token:str
    type:str
    class Config:
        orm_mode = True
    
class TokenPayLoad(BaseModel):
    user_id:int


class Vote(BaseModel):
    post_id: int 
    dir: conint(le = 1)


class VoteResponse(BaseModel):
    Post:PostResponse
    number_of_votes: int 
    class Config:
        orm_mode =  True