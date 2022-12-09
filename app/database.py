from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:anselmo@localhost/social-media-api'

engine = create_engine(SQLALCHEMY_DATABASE_URL)


SesionLocal = sessionmaker(autocommit = False, autoflush = False,bind = engine)



Base = declarative_base()




# Dependency
def get_db():
    # open and close the db 
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()
