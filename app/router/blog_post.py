from ast import Str
from fastapi import APIRouter, Body, Query, Path
from pydantic import BaseModel
from typing import Dict, Optional, List

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    num_comments: int
    publshed: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {"key": "value"}
    image: Optional[Image] = None


@router.post("/new")
def create_blog(blog: BlogModel):
    return {"data": blog}


@router.post("/new/{id}")
def update_blog(blog: BlogModel, id: int, version: int = 1):
    return {"data": blog,
            "id": id,
            "version": version}


@router.post("/new/{id}/comment/{comment_id}")
def create_comment(blog: BlogModel, id: int,
                   comment_title: str = Query(None,
                                              title="Title of the comment",
                                              alias="commentTitle",
                                              description="Some description for comment_title",
                                              deprecated=True),
                   content: str = Body(...,
                                       min_length=10,
                                       max_length=12,
                                       regex="^[a-z\s]*$"),
                   v: Optional[List[str]] = Query(["1.0", "1.1", "1.2"]),
                   comment_id: int = Path(None, gt=5, le=10)
                   ):
    return {"data": blog,
            "id": id,
            "comment_title": comment_title,
            "content": content,
            "version": v,
            "comment_id": comment_id}


def required_functionality():
    return {"message": "Learning FastAPI is important"}
