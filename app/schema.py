from datetime import datetime
from pydantic import BaseModel, EmailStr






# schema REQ
class PostBase(BaseModel): 
    title:str 
    description:str 
    published: bool = True 



class PostCreate(PostBase):
    pass 

    



class PostResponse(PostBase):
    postid:int 
    created_at: datetime

    # allow dict responses to be accepted
    class Config:
        orm_mode = True



# user auth schema 

class User(BaseModel):
    email:EmailStr
    password:str

    

class UserResponse(BaseModel):
    # avoid returning the password to the user
    user_id:int
    email:EmailStr
    class Config:
        orm_mode = True