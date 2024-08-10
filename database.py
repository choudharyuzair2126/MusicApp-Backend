
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


DataBase_url = "mysql+mysqldb://root@localhost/usersdata"
engine = create_engine(DataBase_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False , bind= engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()   

