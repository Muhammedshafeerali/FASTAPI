from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    def bcrypto(Password:str):
        return pwd_context.hash(Password)

    def verify(plainpassword,hashpassword):
        return pwd_context.verify(plainpassword,hashpassword)
