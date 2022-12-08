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
    title:str 
    description:str 
    published: bool = True 


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




@app.get("/")
def read_root():
    return {"Hello": "anselmo you are the best backend engineer"}


@app.get('/posts')
async def get_posts():
    cursor.execute("""SELECT * FROM posts; """)

    posts =  cursor.fetchall()
    return {"data":posts}



@app.post("/post")
async def create_post(post:Post):
    cursor.execute(""" INSERT INTO posts (title, description, published) VALUES (%s, %s, %s) RETURNING * """,(post.title,post.description,post.published))
    # return the post 
    new_post = cursor.fetchone()
    # commint the changes to the db 
    conn.commit()
    return {"data":new_post}


# @app.get("/posts/{id}")
# def get_one_post(id:str,response = Response):
#     print(id)
  
#     return {"post":my_posts[id]}

# @app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delette_post(id:int):
#     for i,p in enumerate(my_posts):
#         if p["id"] == id:
#             return i
#     my_posts.pop(i)   
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# @app.put("posts/{id}")
# def update_post(id:int,post:Post ):

#     return {"msg":"update"}

