from fastapi import FastAPI,Depends,status,Response,HTTPException
from . import models,shema
from sqlalchemy.orm import session

from .database import engine,SessionLocal


models.Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/blog")
def Blog(db:session=Depends(get_db)):
    blogs=db.query(models.Blog).all()

    return blogs


@app.get("/blog/{id}")
def get_blog(id,response:Response,db:session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} is not available")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"message":f"Blog wiht id {id} is not available"}
    return blog  


@app.post("/blog",status_code=status.HTTP_201_CREATED)
def create_blog(request:shema.Blog,db:session=Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return{"data":new_blog}


@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delet_blog(id,db:session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blod with id {id} is not found")
    
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail":"succesfully delete"}


@app.put("/blog/{id}",status_code=status.HTTP_202_ACCEPTED)
def update_blog(id,request:shema.Blog,db:session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {id} is not found")
    blog.update(request.dict())
    db.commit()
    return {"detail":"updated successfully"}