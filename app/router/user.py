from fastapi import APIRouter, Depends
from schemas import UserBase, UserResponse
from sqlalchemy.orm.session import Session
from data.database import get_db
from data import db_user

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

# Create new user


@router.post("/", response_model=UserResponse)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

# TODO: Retrieve user

# TODO: Update user

# TODO: Delete user
