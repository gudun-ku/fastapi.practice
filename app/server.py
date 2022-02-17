from fastapi import FastAPI, Response, status
from enum import Enum
from typing import Optional


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


app = FastAPI()


@app.get("/", tags=["common"])
def index():
    return {"message": "Hello, World"}


@app.get("/blog/all", tags=["blog"], summary="Get all blogs",
         description="Retrieve all existing blogs on the server",
         response_description="The list of available blogs")
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {"message": f"All {page_size} blogs on page {page}"}


@app.get("/blog/{id}/comments/{comment_id}", tags=["blog", "comment"])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving a comment of the blog
    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional query parameter
    """
    return {"message": f"Blog with id {id}, comment with id {comment_id}, valid: {valid}, username: {username}"}


@app.get("/blog/type/{type}", tags=["blog"])
def get_blog_type(type: BlogType):
    return {"message": f"Blog type: {type}"}


@app.get("/blog/{id}", status_code=status.HTTP_200_OK, tags=["blog"])
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog with id: {id} not found!"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with id: {id}"}


@app.post("/hello", tags=["common"])
def hello():
    return "Hi!"
