from typing import Optional
from fastapi import  Depends, FastAPI, Response, status
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel
from random import randrange
import time
from sqlalchemy.orm import session
from . import models
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)


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




@app.get("/")
def read_root():
    return {"Hello": "anselmo you are the best backend engineer"}


# app.get("/sqlalchemy")
# def test(db:session = Depends(get_db)):
#     posts = db.query(models.Post).all()

#     return {"test":posts}



@app.get('/posts')
async def get_posts(db:session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data":posts}



@app.post("/post")
async def create_post(post:Post):
    cursor.execute(""" INSERT INTO posts (title, description, published) VALUES (%s, %s, %s) RETURNING * """,(post.title,post.description,post.published))
    # return the post 
    new_post = cursor.fetchone()
    # commint the changes to the db 
    conn.commit()
    return {"data":new_post}




@app.get("/posts/{postid}")
async def get_one_post(postid:int):

    cursor.execute(""" SELECT * FROM posts WHERE postid = %s""",(str(postid))) 
    post = cursor.fetchone()

    return {"post":post}




@app.delete("/posts/{postid}",status_code=status.HTTP_204_NO_CONTENT)
async def delette_post(postid:int):
    cursor.execute(""" DELETE  FROM posts WHERE postid = %s RETURNING * """, (str(postid)))

    cursor.fetchone()
    conn.commit()

    return {"date":f"deleted item with index {postid}sucessfully "}




@app.put("/posts/{postid}")
async def update_post(postid:int,post:Post ):

    cursor.execute(""" UPDATE posts SET title = %s, description = %s, published = %s WHERE postid = %s  RETURNING * """, (post.title, post.description, post.published, str(postid)))
    updated = cursor.fetchone()
    conn.commit()
    return {"data":updated}

