# https://fastapi.tiangolo.com/tutorial/first-steps/
# How to run the code: uvicorn app.main:app --reload

from random import randrange
import time

from fastapi import FastAPI

import psycopg2 as pg
from psycopg2.extras import RealDictCursor

from . import models
from .database import engine

from .routers import post, user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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

app.include_router(post.router)
app.include_router(user.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
