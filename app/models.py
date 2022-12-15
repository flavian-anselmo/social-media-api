from .database import Base
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts"

    # fields
    postid = Column(Integer,primary_key = True, nullable = False)
    title = Column(String, nullable = False)
    description = Column(String, nullable = False)
    published = Column(Boolean, server_default = 'TRUE', nullable = False)
    created_at = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))
    owner_id = Column(Integer, ForeignKey("users.user_id", ondelete ="CASCADE"), nullable = False) # one to many 
    # fetch the user in regards to the owner _id 
    owner = relationship("User") # return the user 



# user auth 


class User(Base):
    __tablename__ = "users"
    user_id =  Column(Integer, primary_key = True, nullable = False)
    email = Column(String , nullable = False, unique =  True )
    password = Column(String, nullable = False)
    created_at =  Column (TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))