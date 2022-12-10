from datetime import datetime
from pydantic import BaseModel

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