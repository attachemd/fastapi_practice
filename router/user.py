from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import db_user
from db.database import get_db
from schemas import UserBase, UserDisplay

router = APIRouter(prefix="/user", tags=["user"])


# Create user
@router.post("/", response_model=UserDisplay)
async def create_user(
    request: UserBase, db: Session = Depends(get_db)
):
    return db_user.create_user(db, request)


# Read all users
@router.get("/", response_model=List[UserDisplay])
async def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


# Read one user
@router.get("/{user_id}", response_model=UserDisplay)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db, user_id)


# Update user
@router.post("/{user_id}/update")
async def update_user(
    user_id: int, request: UserBase, db: Session = Depends(get_db)
):
    return db_user.update_user(db, user_id, request)


# Delete user
@router.get("/{user_id}/delete")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, user_id)
