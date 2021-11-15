from datetime import datetime
from pydantic import BaseModel

class PostBase(BaseModel):
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


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at:datetime
    class Config:
        orm_mode = True