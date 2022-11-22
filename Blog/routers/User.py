from fastapi import APIRouter,status,Depends,HTTPException
from typing import List
from .. import models,shema,database,hashing
from sqlalchemy.orm import session
from ..repository import Blog,User

Hash=hashing.Hash
router=APIRouter(
    prefix='/user',
    tags=['Users']
)

get_db=database.get_db




@router.post("",status_code=status.HTTP_201_CREATED,response_model=shema.relationUser)
def create_user(request:shema.User,db:session=Depends(get_db)):
    return User.create(request,db)


@router.get("",response_model=List[shema.relationUser])
def users(db:session=Depends(get_db)):
    return User.get_all(db)
   
@router.get("/{id}",response_model=shema.showUser)
def get_user(id:int,db:session=Depends(get_db)):
    return User.show(id,db)
    