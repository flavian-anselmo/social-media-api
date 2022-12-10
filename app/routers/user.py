from fastapi import Depends, HTTPException, status, APIRouter
from app import models, schema
from app.database import get_db
from app.utils import get_pswd_hash, verify_pswd
from sqlalchemy.orm import session

router = APIRouter()

@router.post("/users", status_code = status.HTTP_201_CREATED, response_model= schema.UserResponse)
async def create_user(user:schema.UserCreate, db: session = Depends(get_db)):

    # hash the pswd 
    hashed_password = get_pswd_hash(user.password)
    verify = verify_pswd(user.password, hashed_password)
    if not verify:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail="Invalid password")
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



@router.get("/users/{user_id}", response_model = schema.UserResponse)
async def get_user_id (user_id: int, db:session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="user not found")
    return user