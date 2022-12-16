from fastapi import APIRouter, Depends, HTTPException, status
from app import oauth2
from sqlalchemy.orm import session
from app import models, schema
from app.database import get_db


router = APIRouter(
    prefix = "/api/v1/vote",
    tags =  ["Vote"]
)



@router.post('/', status_code=status.HTTP_201_CREATED)
def  vote(vote:schema.Vote, db:session = Depends(get_db), curr_user:int = Depends(oauth2.get_current_user)):
    post =  db.query(models.Post).filter(models.Post.postid ==  vote.post_id ).first()

    if not post:
        # chec if the posts is available
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="post does not exist")

    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == curr_user.user_id)    
    found_vote = vote_query.first()
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="post already voted")
        new_vote = models.Vote(post_id = vote.post_id, user_id = curr_user.user_id)     
        db.add(new_vote)
        db.commit()
        db.refresh(new_vote)
        return {"msg":"successfully voted"}
    else:
        if not found_vote:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="vote does not exist")
        vote_query.delete(synchronize_session =  False) 
        db.commit()
        return {"msg":"vote deleted"}       
