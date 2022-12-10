from pydantic import BaseModel

# schema 
class Post(BaseModel): 
    title:str 
    description:str 
    published: bool = True 



class CreatePost(BaseModel):
    title:str 
    description:str 
    published: bool = True 

    
class UpdatePost(BaseModel):
    title:str 
    description:str 
    published: bool


