from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()


# this validates if the user provides the correct data type
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "Post 1", "content": "This is the content of post 1", "published": True, "id": 1},
            {"title": "Post 2", "content": "This is the content of post 2", "published": False, "id": 2},
            {"title": "Post 3", "content": "This is the content of post 3", "published": True, "id": 3}]


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict["id"] = randrange(1, 100000)
    my_posts.append(post.model_dump())
    return {"data": post_dict}
