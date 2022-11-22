from fastapi import status,Depends,HTTPException
from typing import List
from .. import models,shema,hashing,database
from sqlalchemy.orm import session

Hash=hashing.Hash

get_db=database.get_db

def create(request:shema.User,db:session):
    user=models.User(name=request.name,email=request.email,password=Hash.bcrypto(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_all(db:session):
    blog=db.query(models.User).all()
    return blog

def show(id:int,db:session):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} is not found")
    
    return user