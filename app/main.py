from typing import Optional
from fastapi import  Depends, FastAPI, HTTPException, Response, status
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel
from random import randrange
import time
from sqlalchemy.orm import session

from app.schema import Post
from . import models, schema
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)


# entry to the application 
app = FastAPI()










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
async def create_post(post:schema.Post, db:session = Depends(get_db)):

    # cursor.execute(""" INSERT INTO posts (title, description, published) VALUES (%s, %s, %s) RETURNING * """,(post.title,post.description,post.published))
    # # return the post 
    # new_post = cursor.fetchone()
    # # commint the changes to the db 
    # conn.commit()

   #new_post =  models.Post( title = post.title,description = post.description,published = post.published)
   # commit 
   new_post =  models.Post( **post.dict())

   db.add(new_post)
   db.commit()
   db.refresh(new_post)
   return {"data":new_post}





@app.get("/posts/{postid}")
async def get_one_post(postid: int, db:session =  Depends(get_db)):

    # cursor.execute(""" SELECT * FROM posts WHERE postid = %s""",(str(postid))) 
    # post = cursor.fetchone()
   post = db.query(models.Post).filter(models.Post.postid == postid).first()
   return {"data":post}



@app.delete("/posts/{postid}",status_code=status.HTTP_204_NO_CONTENT)
async def delette_post(postid:int, db:session =  Depends(get_db)):
    # cursor.execute(""" DELETE  FROM posts WHERE postid = %s RETURNING * """, (str(postid)))

    # cursor.fetchone()
    # conn.commit()
    post = db.query(models.Post).filter(models.Post.postid == postid)
    post.first()
    post.delete(synchronize_session = False)
    db.commit()    
    return {"date":f"deleted item with index {postid}sucessfully "}




@app.put("/posts/{postid}")
async def update_post(postid: int, post_update:schema.Post, db: session = Depends(get_db) ):
    # cursor.execute(""" UPDATE posts SET title = %s, description = %s, published = %s WHERE postid = %s  RETURNING * """, (post.title, post.description, post.published, str(postid)))
    # updated = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.postid == postid)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="post not found")
    post_query.update(post_update.dict(), synchronize_session = False)
    db.commit()
    return {"data": post_query.first()}

