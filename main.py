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

my_posts = [{"title": "Post 1", "content": "This is the content of post 1", "published": True, "rating": 5},
            {"title": "Post 2", "content": "This is the content of post 2", "published": False, "rating": 4},
            {"title": "Post 3", "content": "This is the content of post 3", "published": True, "rating": 3}]


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts ")
def create_posts(new_post: Post):
    print(new_post) # this will print the pydantic model
    print(new_post.dict()) # this will conver pydantic model to dictionary
    return {"data": new_post}
