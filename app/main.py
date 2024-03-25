from fastapi import FastAPI, responses, status, HTTPException, Depends
from fastapi import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session

#  this created table in the database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="fastapi",
            user="postgres",
            password="postgres",
            cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Connected to the database!!!")
        break
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        time.sleep(5)


@app.get("/posts",  response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    post = db.query(models.Post).all()
    return post

@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.get("/posts/{id}")
def get_post(id: int, response: responses.Response, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    deleted_post = db.query(models.Post).filter(models.Post.id == id)
    if deleted_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    db.delete(deleted_post, synchronize_session=False)
    db.commit()
    return responses.Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, response: responses.Response, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()



#################USER####################

@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user