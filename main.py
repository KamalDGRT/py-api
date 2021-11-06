# https://fastapi.tiangolo.com/tutorial/first-steps/

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


class Post(BaseModel):
    """
    A pydantic model that does the part of data
    validation.

    It is because of this we can ensure that whatever
    data is sent by the frontend is in compliance
    with the backend.
    """
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {
        "title": "title of post 1",
        "content": "content of post 1",
        "id": 1
    },
    {
        "title": "favorite foods",
        "content": "I like pizza",
        "id": 2
    }
]


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/posts')
def get_posts():
    return {
        "data": my_posts
    }
