from fastapi import FastAPI
from fastapi import Body

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/create_posts")
def create_posts(payload: dict = Body(...)):
    return {"new_post": f"title: {payload['title']}, content: {payload['content']}"}