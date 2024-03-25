from fastapi import status, HTTPException, Depends, Response, APIRouter
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils

router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login", status_code=status.HTTP_200_OK)
def login(user_credentials: schemas.UserLogin, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not utils.verify(user_credentials.password.encode(), user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    return {"message": "example token"}