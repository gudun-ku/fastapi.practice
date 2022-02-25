from pydantic import BaseModel
from typing import List


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserPopulate(BaseModel):
    id: int
    username: str

    class Config():
        orm_mode = True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class ArticlePopulate(BaseModel):
    title: str
    published: bool

    class Config():
        orm_mode = True


class ArticleResponse(BaseModel):
    title: str
    content: str
    published: bool
    user: UserPopulate

    class Config():
        orm_mode = True


class UserResponse(BaseModel):
    username: str
    email: str
    items: List[ArticlePopulate] = []

    class Config():
        orm_mode = True
