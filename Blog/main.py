from fastapi import FastAPI
from . import models,shema
from .database import engine,SessionLocal,get_db
from .routers import Blog,User


models.Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(Blog.router)
app.include_router(User.router)

