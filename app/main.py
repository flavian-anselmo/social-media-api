from typing import Optional
from fastapi import  FastAPI, Response, status
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel
from random import randrange
import time



# entry to the application 
app = FastAPI()



class Post(BaseModel):
    #schema 
    # how the post api should look like 
    # validation 
    title:str 
    content:str 
    published: Optional[bool] = True # optional
while True:    
    try:
        conn = psycopg2.connect(host='localhost',database='social-media-api',user='postgres',password='anselmo', cursor_factory=RealDictCursor)     
        cursor = conn.cursor()
        print('DB connection was successfull')
        break
    except Exception as    error:
        print('connetion failed ')
        print(error)
        time.sleep(5)



# like our db 
my_posts = [    {
        "title":"psodt 1 ",
        "content":"desc 1",
        "published":True,
    },
]



@app.get("/")
def read_root():
    return {"Hello": "anselmo you are the best backend engineer"}


@app.get('/posts')
async def get_posts():
    cursor.execute("""SELECT * FROM posts; """)

    posts =  cursor.fetchall()
    return {"data":posts}



@app.post("/post")
def create_post(new_post:Post):
    post_dict = new_post.dict()
    post_dict["id"] = randrange(0,1000000)
    my_posts.append(post_dict)


    return {"data":post_dict}


# @app.get("/posts/{id}")
# def get_one_post(id:str,response = Response):
#     print(id)
  
#     return {"post":my_posts[id]}

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delette_post(id:int):
    for i,p in enumerate(my_posts):
        if p["id"] == id:
            return i
    my_posts.pop(i)   
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# @app.put("posts/{id}")
# def update_post(id:int,post:Post ):

#     return {"msg":"update"}

