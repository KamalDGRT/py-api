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


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# This is the content that I gave in the Body -> Raw -> JSON in the Postman
#  Feel free to test out with vallues of different types.
# {
#     "title": "Yii2 Framework",
#     "content": "Yii2 is one of the top 5 PHP Frameworks",
#     "rating": 4
# }
@app.post('/createpost')
def create_post(post: Post):
    post.dict()   # Converts a pydantic model to a dictionary
    return {
        "data": post
    }
