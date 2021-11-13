# https://fastapi.tiangolo.com/tutorial/first-steps/
# How to run the code: uvicorn app.main:app --reload

from fastapi import FastAPI, status, HTTPException, Response
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2 as pg
from psycopg2.extras import RealDictCursor
import time


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


# Looping till we get a connection and breaking out of it
# once the connection is established.
while True:
    try:
        conn = pg.connect(
            host='localhost',
            database='py_api',
            user='postgres',
            password='',
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database connection was successfull!")
        break
    except Exception as error:
        print('Connection to the database failed!')
        print('Error: ', error)
        time.sleep(2)


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


def find_post(id):
    for post in my_posts:
        if post['id'] == id:
            return post


def find_index_post(id):
    for index, post in enumerate(my_posts):
        if post['id'] == id:
            return index


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/posts')
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {
        "data": posts
    }


@app.post('/post/create', status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    """
    Inserting a new post into the database
    """
    cursor.execute(
        """INSERT into posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
        (post.title, post.content, post.published)
    )
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}


@app.get('/post/{id}')
def get_post(id: int):
    """ 
    {id} is a path parameter
    """
    cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id), ))
    # We are
    # - taking an string from the parameter
    # - converting it to int
    # - then again converting it to str
    # We are doing this because we want to valid that the user is giving
    # only integers in the argument and not string like `adfadf`.
    # Plus we are adding a comma after the str(id) because we run into an
    # error later. Don't know the reason for the error yet.
    post = cursor.fetchone()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} not found!")
    return { "post_detail": post }


@app.delete('/post/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # find the index in the array that has the required id
    # my_posts.pop(index)
    index = find_index_post(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} does not exist!")

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# make sure to add some body in the postman to check it.
@app.put('/post/update/{id}')
def update_post(id: int, post: Post):
    index = find_index_post(id)

    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} does not exist!")

    post_dict = post.dict()  # take all data from frotend
    post_dict['id'] = id   # add the id
    my_posts[index] = post_dict  # updating the post in the array using index

    return {
        'data': post_dict
    }
