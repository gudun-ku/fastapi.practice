from typing import List
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

# Retrieve user


@router.get("/", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


@router.get("/{id}", response_model=UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db, id)

# Update user


@router.put("/{id}")
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(db, id, request)

# Delete user


@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, id)
