import uuid
import bcrypt
from fastapi import Depends, HTTPException, Header
from middleware.middle_ware import auth_middleware
from models.user import User
from pydantic_schemas.user_create import CreateUser
from pydantic_schemas.user_login import Userlogin

from fastapi import APIRouter
from database import get_db
from sqlalchemy.orm import Session,joinedload

import jwt

router = APIRouter()
@router.post('/signup',status_code=201)
def signup_user(users: CreateUser,db:Session = Depends(get_db)):

    # Check if the user is already signed up 

    user_db = db.query(User).filter(User.email == users.email).first()

    if user_db:
        raise HTTPException(400,"User already exists")
        
    
    hashed_pw = bcrypt.hashpw(users.password.encode('utf-8'), bcrypt.gensalt())

    user_id = str(uuid.uuid4())

    user_db = User(id = user_id , name = users.name, email = users.email,password = hashed_pw)
    # create a new user and add it to the database
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db


@router.post('/login',)
def login_user(users: Userlogin,db: Session = Depends(get_db)):
    user_db = db.query(User).filter(User.email == users.email).first()
    if not user_db:
        raise HTTPException(status_code = 400, detail = "User not found")
    is_match = bcrypt.checkpw(users.password.encode('utf-8'), user_db.password)
    if not is_match:    
        raise HTTPException(status_code = 400, detail = "Incorrect password")
    
    token = jwt.encode({'id':user_db.id,},'password_key')
    return {'token':token ,'user':user_db }
    
@router.get('/')
def current_user_data(db:Session = Depends(get_db),
                      user_dict = Depends(auth_middleware)):
   user = db.query(User).filter(User.id == user_dict['uid']).options(joinedload(User.favorites)).first()

   if not user:
       raise HTTPException(status_code = 400, detail = "User not found")
   return user