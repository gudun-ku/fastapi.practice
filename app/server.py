import imp
from fastapi import FastAPI
from router import blog_get, blog_post, user
from data import models
from data.database import engine

app = FastAPI()
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/", tags=["common"])
def index():
    return {"message": "Hello, World"}


models.Base.metadata.create_all(engine)
