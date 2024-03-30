from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, database, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

#SECRET KEY
#Algorithm used to encode the token
#Expiration time of the token

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


#Oto opis funkcji:
#create_access_token(data: dict): Ta funkcja tworzy token dostępu na podstawie przekazanych danych. Przyjmuje słownik data jako argument, który zawiera dane, które mają być zakodowane w tokenie. Funkcja tworzy kopię tego słownika, dodaje do niego czas wygaśnięcia tokena, koduje go przy użyciu algorytmu ALGORITHM i klucza SECRET_KEY, a następnie zwraca zakodowany token.
#verify_access_token(token: str, credentials_exception): Ta funkcja weryfikuje token dostępu. Przyjmuje token jako argument token oraz wyjątek credentials_exception, który zostanie podniesiony, jeśli weryfikacja nie powiedzie się. Funkcja dekoduje token przy użyciu klucza SECRET_KEY i algorytmu ALGORITHM, a następnie pobiera identyfikator użytkownika z zdekodowanego payloadu. Jeśli identyfikator nie istnieje, zostanie podniesiony wyjątek credentials_exception. Na koniec funkcja tworzy obiekt TokenData na podstawie identyfikatora użytkownika.

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    
    return token_data
    
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},)
    
    token = verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user