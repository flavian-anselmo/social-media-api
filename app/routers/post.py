from typing import List, Optional
from app.database import  get_db
from .. import models, schema
from fastapi import  APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import session
from app import oauth2
from sqlalchemy import func



router = APIRouter(
    prefix="/api/v1/posts",
    tags = ["post"]
)






@router.get('/',response_model = List[schema.VoteResponse])
async def get_posts(
    db:session = Depends(get_db),
    current_user:int = Depends(oauth2.get_current_user),
    limit: int = 10,
    skip:int = 0,
    search:Optional[str] = ''
):
    # get all posts 
    print(limit)
    # query parameters with sql

    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    results = db.query(models.Post, func.count(models.Vote.post_id).label("number_of_votes")).join(models.Vote, models.Vote.post_id == models.Post.postid, isouter = True).group_by(models.Post.postid).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    print(results)
    return results



@router.post("/",response_model = schema.PostResponse, status_code = status.HTTP_201_CREATED)
async def create_post(post:schema.PostCreate, db:session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):

    # cursor.execute(""" INSERT INTO posts (title, description, published) VALUES (%s, %s, %s) RETURNING * """,(post.title,post.description,post.published))
    # # return the post 
    # new_post = cursor.fetchone()
    # # commint the changes to the db 
    # conn.commit()

   #new_post =  models.Post( title = post.title,description = post.description,published = post.published)
   # commit 
   print(current_user.user_id)
   new_post =  models.Post(owner_id = current_user.user_id, **post.dict())

   db.add(new_post)
   db.commit()
   db.refresh(new_post)
   return new_post




@router.get("/{postid}",response_model = schema.VoteResponse)
async def get_one_post(postid: int, db:session =  Depends(get_db),user_id:int = Depends(oauth2.get_current_user)):

    # cursor.execute(""" SELECT * FROM posts WHERE postid = %s""",(str(postid))) 
    # post = cursor.fetchone()
   post = db.query(models.Post, func.count(models.Vote.post_id).label("number_of_votes")).join(models.Vote, models.Vote.post_id == models.Post.postid, isouter = True).group_by(models.Post.postid).filter(models.Post.postid == postid).first()
   return post



@router.delete("/{postid}",status_code=status.HTTP_204_NO_CONTENT)
async def delette_post(postid:int, db:session =  Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" DELETE  FROM posts WHERE postid = %s RETURNING * """, (str(postid)))

    # cursor.fetchone()
    # conn.commit()
    post = db.query(models.Post).filter(models.Post.postid == postid)
    owner_id = post.first().owner_id
    print( current_user.user_id)
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "post not found")
    if owner_id != current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authoised to Perform Request")
    post.delete(synchronize_session = False)
    db.commit()    
    return {"date":f"deleted item with index {postid}sucessfully "}




@router.put("/{postid}",response_model = schema.PostResponse)
async def update_post(postid: int, post_update:schema.PostCreate, db: session = Depends(get_db), user_id:int = Depends(oauth2.get_current_user)):
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
