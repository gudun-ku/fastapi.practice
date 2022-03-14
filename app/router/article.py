from click import get_current_context
from fastapi import APIRouter, Depends
from schemas import ArticleBase, ArticleResponse, UserBase
from sqlalchemy.orm import Session
from data.database import get_db
from data import db_article
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix="/article",
    tags=["article"]
)

# Create article


@router.post("/", response_model=ArticleResponse)
def create_article(request: ArticleBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_article.create_article(db, request)


@router.get("/{id}")  # , response_model=ArticleResponse)
def get_article(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
        "data": db_article.get_article(db, id),
        "current_user": current_user
    }
