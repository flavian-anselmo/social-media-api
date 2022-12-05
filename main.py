from typing import Optional
from fastapi import  FastAPI, Response, status
from pydantic import BaseModel
from random import randrange
app = FastAPI()



class Post(BaseModel):
    #schema 
    # how the post api should look like 
    # validation 
    title:str 
    desc:str 
    published: bool = True # optional 
    rating: Optional [int] = None 


# like our db 
my_posts = [    {
        "title":"psodt 1 ",
        "desc":"desc 1",
        "published":True,
        "rating": 4,
        "id":1,
    },
]



@app.get("/")
def read_root():
    return {"Hello": "anselmo you are the best backend engineer"}


@app.get('/posts')
def get_posts():
    return {"data":my_posts}



@app.post("/post")
def create_post(new_post:Post):
    post_dict = new_post.dict()
    post_dict["id"] = randrange(0,1000000)
    my_posts.append(post_dict)


    return {"data":post_dict}


@app.get("/posts/{id}")
def get_one_post(id:int,response = Response):
    print(id)
    if not id:
        response.status_code = status.HTTP_404_NOT_FOUND
        
    return {"post":my_posts[id]}

