from typing import List
from app.database import  get_db
from .. import models, schema
from fastapi import  APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import session



router = APIRouter(
    prefix="/api/v1/posts",
)






@router.get('/',response_model = List[schema.PostResponse])
async def get_posts(db:session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts



@router.post("/",response_model = schema.PostResponse, status_code = status.HTTP_201_CREATED)
async def create_post(post:schema.PostCreate, db:session = Depends(get_db)):

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
   return new_post




@router.get("/{postid}",response_model = schema.PostResponse)
async def get_one_post(postid: int, db:session =  Depends(get_db)):

    # cursor.execute(""" SELECT * FROM posts WHERE postid = %s""",(str(postid))) 
    # post = cursor.fetchone()
   post = db.query(models.Post).filter(models.Post.postid == postid).first()
   return post



@router.delete("/{postid}",status_code=status.HTTP_204_NO_CONTENT)
async def delette_post(postid:int, db:session =  Depends(get_db)):
    # cursor.execute(""" DELETE  FROM posts WHERE postid = %s RETURNING * """, (str(postid)))

    # cursor.fetchone()
    # conn.commit()
    post = db.query(models.Post).filter(models.Post.postid == postid)
    post.first()
    post.delete(synchronize_session = False)
    db.commit()    
    return {"date":f"deleted item with index {postid}sucessfully "}




@router.put("/{postid}",response_model = schema.PostResponse)
async def update_post(postid: int, post_update:schema.PostCreate, db: session = Depends(get_db) ):
    # cursor.execute(""" UPDATE posts SET title = %s, description = %s, published = %s WHERE postid = %s  RETURNING * """, (post.title, post.description, post.published, str(postid)))
    # updated = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.postid == postid)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="post not found")
    post_query.update(post_update.dict(), synchronize_session = False)
    db.commit()
    return post_query.first()
