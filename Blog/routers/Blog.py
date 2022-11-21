from fastapi import APIRouter,Depends,HTTPException,status,Response
from typing import List
from sqlalchemy.orm import session
from  .. import shema,models,database

router=APIRouter(
    prefix="/blog",
    tags=['blogs']
)

get_db=database.get_db

@router.get("",response_model=List[shema.ShowBlog])
def Blog(db:session=Depends(get_db)):
    blogs=db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Blogs not found")

    return blogs



@router.get("/{id}",response_model=shema.ShowBlog)
def get_blog(id,response:Response,db:session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} is not available")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"message":f"Blog wiht id {id} is not available"}
    return blog  

@router.post("",status_code=status.HTTP_201_CREATED)
def create_blog(request:shema.Blog,db:session=Depends(get_db),user_id=1):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return{"data":new_blog}


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delet_blog(id,db:session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blod with id {id} is not found")
    
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail":"succesfully delete"}


@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update_blog(id,request:shema.Blog,db:session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {id} is not found")
    blog.update(request.dict())
    db.commit()
    return {"detail":"updated successfully"}
