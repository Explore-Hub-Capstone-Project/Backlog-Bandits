from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from pymongo.database import Database
from app.schemas import UserDisplay, UserCreate, LoginDisplay, UserGet, LoginSchema
from app.db.database import get_db

# from app.db.db_user import create_user, get_all_users, get_user, update_user, delete_user
from app.db import db_user
from app.db.hash import Hash
from app.db.db_user import authenticate_user


router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("/", response_model=UserDisplay, status_code=status.HTTP_201_CREATED)
async def register_user(request: UserCreate, db: Database = Depends(get_db)):
    return await db_user.create_user(db, request)


@router.post("/login", response_model=LoginDisplay)
async def login(request: LoginSchema, db: Database = Depends(get_db)):
    response = await db_user.authenticate_user(db, request.email, request.password)
    return response


@router.get("/", response_model=UserDisplay, status_code=status.HTTP_200_OK)
async def read_user_info(request: UserGet = Depends(), db: Database = Depends(get_db)):
    return await db_user.get_user(db, request)


# read one user
@router.get("/{id}", response_model=UserDisplay)
async def get_user(id: str, db: Database = Depends(get_db)):
    return await db_user.get_user(db, UserGet(id=id))
