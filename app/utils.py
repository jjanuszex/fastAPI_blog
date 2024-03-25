from passlib.context import CryptContext # this is for hashing the password

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # this is for hashing the password


def hash(password: str):
    return pwd_context.hash(password) # this is for hashing the password