from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from exceptions import StoryException
from router import blog_get, blog_post, user, article
from data import models
from data.database import engine

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/", tags=["common"])
def index():
    return {"message": "Hello, World"}


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={"detail": exc.name}
    )


@app.exception_handler(HTTPException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.detail}
    )


models.Base.metadata.create_all(engine)
