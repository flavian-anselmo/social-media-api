from fastapi import Depends, HTTPException, status
from jose import  jwt, JWTError
from datetime import datetime, timedelta
from app import models, schema
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import session

from app.database import SesionLocal, get_db


ooauth2_schema = OAuth2PasswordBearer(tokenUrl = 'login')


SECRET_KEY:str = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'

ALGORITHM:str = 'HS256'

ACCESS_TOKEN_EXPIRATION_TIME:int = 1 # expires in 30 minutes



def create_access_token(payload: dict):
    to_encoded_payload = payload.copy()
    expire = datetime.utcnow() +  timedelta(minutes =  ACCESS_TOKEN_EXPIRATION_TIME)

    # update the expiration time

    to_encoded_payload.update({'exp': expire})

    # encode the payload secret and  state the algo

    encoded_jwt =  jwt.encode(to_encoded_payload, SECRET_KEY,ALGORITHM)

    return encoded_jwt



# secret key 
# algorithm used 
# the expiration date


def  verify_access_token(token: str, creds_exceptions):
    
    '''
    verify if the token is valid and if decoded, it can return the exact user id 
    that was created

    '''
    try:
        payload: dict =  jwt.decode(token, SECRET_KEY,ALGORITHM)

        # print(payload)
        user_id:int = payload.get("user_id")
        # print(user_id)


        if user_id is None :
            # if 
            raise creds_exceptions


        # verify with the schema datatype
        token_data = schema.TokenPayLoad(user_id = user_id)

        # print(token_data)
        return token_data

    except JWTError :
        raise creds_exceptions
    return token_data    




def get_current_user(a_token:str = Depends(ooauth2_schema), db: session= Depends(get_db)):
    cred_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Not authenticated",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token = verify_access_token(token = a_token, creds_exceptions = cred_exception)
    user = db.query(models.User).filter(models.User.user_id == token.user_id).first()
    return user 
