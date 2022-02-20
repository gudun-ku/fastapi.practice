from fastapi import APIRouter, Response, status, Depends
from enum import Enum
from typing import Optional

from router.blog_post import required_functionality

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@router.get("/all", summary="Get all blogs",
            description="Retrieve all existing blogs on the server",
            response_description="The list of available blogs")
def get_blogs(page=1, page_size: Optional[int] = None, req_parameter: dict = Depends(required_functionality)):
    return {"message": f"All {page_size} blogs on page {page}", "req": req_parameter}


@router.get("/{id}/comments/{comment_id}", tags=["comment"])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving a comment of the blog
    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional query parameter
    """
    return {"message": f"Blog with id {id}, comment with id {comment_id}, valid: {valid}, username: {username}"}


@router.get("/type/{type}")
def get_blog_type(type: BlogType, req_parameter: dict = Depends(required_functionality)):
    return {"message": f"Blog type: {type}", "req": req_parameter}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog with id: {id} not found!"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with id: {id}"}
