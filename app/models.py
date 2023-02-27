from .database import Base
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship




class User(Base):
    __tablename__ = "users"
    user_id =  Column(Integer, primary_key = True, nullable = False)
    email = Column(String , nullable = False, unique =  True )
    password = Column(String, nullable = False)
    created_at =  Column (TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))


