from fastapi import APIRouter,Depends,HTTPException,status,Response
from typing import List
from sqlalchemy.orm import session
from  .. import shema,models,database,oauth2
from ..repository import Blog,User


router=APIRouter(
    prefix="/blog",
    tags=['blogs']
)

get_db=database.get_db

@router.get("",response_model=List[shema.ShowBlog])
def blog(db:session=Depends(get_db),current_user:shema.relationUser=Depends(oauth2.get_current_user)):
    return Blog.get_all(db)
   



@router.get("/{id}",response_model=shema.ShowBlog)
def get_blog(id:int,response:Response,db:session=Depends(get_db)):
    return Blog.show(id,db)
      

@router.post("",status_code=status.HTTP_201_CREATED)
def create_blog(request:shema.Blog,db:session=Depends(get_db),user_id=1):
    return Blog.create(request,db,user_id)
    


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delet_blog(id,db:session=Depends(get_db)):
    return Blog.delete(id,db)
    


@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update_blog(id,request:shema.Blog,db:session=Depends(get_db)):
    return Blog.update(id,request,db)
   