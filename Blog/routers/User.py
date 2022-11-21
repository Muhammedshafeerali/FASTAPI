from fastapi import APIRouter,status,Depends,HTTPException
from typing import List
from .. import models,shema,database,hashing
from sqlalchemy.orm import session

Hash=hashing.Hash
router=APIRouter(
    prefix='/user',
    tags=['Users']
)

get_db=database.get_db




@router.post("",status_code=status.HTTP_201_CREATED,response_model=shema.showUser)
def create_user(request:shema.User,db:session=Depends(get_db)):
    user=models.User(name=request.name,email=request.email,password=Hash.bcrypto(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("",response_model=List[shema.showUser])
def users(db:session=Depends(get_db)):
    blog=db.query(models.User).all()
    return blog

@router.get("/{id}",response_model=shema.showUser)
def get_user(id:int,db:session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} is not found")
    
    return user