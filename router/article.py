from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import db_article
from db.database import get_db
from schemas import ArticleDisplay, ArticleBase, HTTPError

router = APIRouter(prefix="/article", tags=["article"])


# Create article
@router.post(
    "/",
    response_model=ArticleDisplay,
    responses={
        418: {"model": HTTPError},
    },
)
async def create_article(
    request: ArticleBase, db: Session = Depends(get_db)
):
    return db_article.create_article(db, request)


# Get specific article
@router.get(
    "/{article_id}",
    response_model=ArticleDisplay,
    responses={
        404: {
            "model": HTTPError,
            "description": "Not found response",
        },
    },
)
# @router.get("/{article_id}", response_model=ArticleDisplay)
async def get_article(
    article_id: int, db: Session = Depends(get_db)
):
    return db_article.get_article(db, article_id)


# Get all articles
@router.get("/", response_model=List[ArticleDisplay])
async def get_all_articles(db: Session = Depends(get_db)):
    return db_article.get_all_articles(db)
