# https://fastapi.tiangolo.com/tutorial/first-steps/

from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# This is the content that I gave in the Body -> Raw -> JSON in the Postman
# {
#     "title": "Yii2 Framework",
#     "content": "Yii2 is one of the top 5 PHP Frameworks"
# }
@app.post('/createpost')
def create_post(payLoad: dict = Body(...)):
    print(payLoad)
    return {
        "new_post": f"Title: {payLoad['title']}, Content: {payLoad['content']}"
    }
