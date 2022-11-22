from fastapi import APIRouter,Depends
from .. import shema,models,database
from sqlalchemy.orm import session
from ..repository import Authenticate


router=APIRouter(
    # prefix='/authentication',
    tags=['authentication']
)

@router.post("/login")
def login(request:shema.Login,db:session=Depends(database.get_db)):
    return Authenticate.Login(request,db)
