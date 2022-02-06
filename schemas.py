from typing import List
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class ArticleForUserDisplay(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True


class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[ArticleForUserDisplay] = []

    class Config:
        orm_mode = True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class UserForArticleDisplay(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: UserForArticleDisplay

    class Config:
        orm_mode = True


class HTTPError(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {"detail": "HTTPException raised."},
        }
