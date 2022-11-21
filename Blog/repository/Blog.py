from sqlalchemy.orm import session
from fastapi import HTTPException,status
from .. import models,shema


def get_all(db:session):
    blogs=db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Blogs not found")

    return blogs

def show(id:int,db:session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} is not available")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"message":f"Blog wiht id {id} is not available"}
    return blog

def create(request:shema.Blog,db:session):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return{"data":new_blog}

def delete(id:int,db:session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blod with id {id} is not found")
    
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail":"succesfully delete"}


def update(id:int,request:shema.Blog,db:session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {id} is not found")
    blog.update(request.dict())
    db.commit()
    return {"detail":"updated successfully"}
