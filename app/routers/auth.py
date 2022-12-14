from fastapi import APIRouter,Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import session
from app import schema, models, utils,oauth2
from app.database import get_db







router = APIRouter(tags=['Authentiction'])


@router.post('/login')
async def login( user_creds:OAuth2PasswordRequestForm =  Depends(), db: session = Depends(get_db)):
    """
    this is thre structure oauth will use to get user credentials

    {
        "username": "admin",
        "password": "admin"
    }
    """
    user = db.query(models.User).filter(models.User.email == user_creds.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid CRedentials")

    if not utils.verify_pswd(user_creds.password, user.password ):
        #verify the password 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="INvalid CRedentials")


    # create a token 
    # return token 
    access_token = oauth2.create_access_token(payload = {"user_id": user.user_id})

    return {"access_token":access_token, "type": "Bearer"}

