from pydantic import BaseModel

# schema 
class PostBase(BaseModel): 
    title:str 
    description:str 
    published: bool = True 



class PostCreate(PostBase):
    pass 

    



