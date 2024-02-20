from typing import List
from app.schemas import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.db import db_user

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


# create user
@router.post("/", response_model=UserDisplay)
async def create_user(request: UserBase, db: AsyncSession = Depends(get_db)):
    return await db_user.create_user(db, request)


# read all users
@router.get("/", response_model=List[UserDisplay])
async def get_all_users(db: AsyncSession = Depends(get_db)):
    return await db_user.get_all_users(db)


# read one user
@router.get("/{id}", response_model=UserDisplay)
async def get_user(id: int, db: AsyncSession = Depends(get_db)):
    return await db_user.get_user(db, id)


# update user
@router.post("/{id}/update")
async def update_user(id: int, request: UserBase, db: AsyncSession = Depends(get_db)):
    return await db_user.update_user(db, id, request)


# delete user
@router.get("/delete/{id}")
async def delete(id: int, db: AsyncSession = Depends(get_db)):
    return await db_user.delete_user(db, id)
