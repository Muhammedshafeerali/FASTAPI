from pydantic import BaseModel
from typing import Optional
from typing import List

class Blog(BaseModel):
    title:str
    body:str
    
    # published:Optional[bool]

class relationBlog(Blog):
    class Config():
        orm_mode=True


class User(BaseModel):
    name:str
    email:str
    password:str

class relationUser(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode=True

class showUser(BaseModel):
    name:str
    email:str
    blogs:List[relationBlog]
    class Config():
        orm_mode=True


class ShowBlog(BaseModel):
    title:str
    body:str
    creator:relationUser
    class Config():
        orm_mode=True
