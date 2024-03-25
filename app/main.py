from fastapi import FastAPI, responses, status, HTTPException, Depends
from fastapi import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post, user, auth

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

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)