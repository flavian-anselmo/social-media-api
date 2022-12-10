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



# old version of connection to  the database

# while True:    
#     try:
#         conn = psycopg2.connect(host='localhost',database='social-media-api',user='postgres',password='anselmo', cursor_factory=RealDictCursor)     
#         cursor = conn.cursor()
#         print('DB connection was successfull')
#         break
#     except Exception as    error:
#         print('connetion failed ')
#         print(error)
#         time.sleep(5)
