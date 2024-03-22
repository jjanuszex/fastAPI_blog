from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# this validates if the user provides the correct data type
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post) # this will print the pydantic model
    print(new_post.dict()) # this will conver pydantic model to dictionary
    return {"data": new_post.dict()}
