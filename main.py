from fastapi import FastAPI, responses, status, HTTPException
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

def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post
    return None

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict["id"] = randrange(1,   100000)
    my_posts.append(post.model_dump())
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int, response: responses.Response):
    post = find_post(int(id))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return {"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    my_posts.pop(index)
    return responses.Response(status_code=status.HTTP_204_NO_CONTENT)