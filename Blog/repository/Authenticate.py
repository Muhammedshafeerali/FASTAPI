from fastapi import HTTPException,status
from .. import shema,models,JWTtoken
from sqlalchemy.orm import session
from ..hashing import Hash

def Login(request:shema.Login,db:session):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credential")
    
    if not Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Incorrect Password")

    access_token = JWTtoken.create_access_token(
        data={"sub": user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}

  