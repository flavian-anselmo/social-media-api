from jose import  jwt
from datetime import datetime, timedelta

SECRET_KEY:str = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'

ALGORITHM:str = 'HS256'

ACCESS_TOKEN_EXPIRATION_TIME:int = 30 # expires in 30 minutes



def create_access_token(payload: dict):
    to_encoded_payload = payload.copy()
    expire = datetime.now() +  timedelta(minutes =  ACCESS_TOKEN_EXPIRATION_TIME)

    # update the expiration time

    to_encoded_payload.update({'exp': expire})

    # encode the payload secret and  state the algo

    encoded_jwt =  jwt.encode(to_encoded_payload, SECRET_KEY,ALGORITHM)

    return encoded_jwt



# secret key 
# algorithm used 
# the expiration date


