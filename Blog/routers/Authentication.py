from fastapi import APIRouter,Depends
from .. import shema,models,database
from sqlalchemy.orm import session
from ..repository import Authenticate
from fastapi.security import OAuth2PasswordRequestForm


router=APIRouter(
    # prefix='/authentication',
    tags=['authentication']
)

@router.post("/login")
def login(request:OAuth2PasswordRequestForm = Depends(),db:session=Depends(database.get_db)):
    return Authenticate.Login(request,db)
