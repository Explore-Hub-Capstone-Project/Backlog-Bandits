from typing import List
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from pymongo.database import Database
from app.schemas import (
    UserDisplay,
    UserCreate,
    LoginDisplay,
    UserGet,
    LoginSchema,
    User,
)
from app.db.database import get_db
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.jwttoken import verify_token

# from app.db.db_user import create_user, get_all_users, get_user, update_user, delete_user
from app.db import db_user
from app.db.hash import Hash
from app.db.db_user import authenticate_user


router = APIRouter(
    prefix="/user",
    tags=["user"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)], db: Database = Depends(get_db)
):

    id_email = verify_token(
        token,
        HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=" not authorized.",
        ),
    )

    user: User = await db_user.get_user(db, UserGet(id=id_email["id"]))
    return user


@router.post("/", response_model=UserDisplay, status_code=status.HTTP_201_CREATED)
async def register_user(request: UserCreate, db: Database = Depends(get_db)):
    return await db_user.create_user(db, request)


@router.post("/login", response_model=LoginDisplay)
async def login(
    request: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Database = Depends(get_db),
):
    response = await db_user.authenticate_user(db, request.username, request.password)
    return response


@router.get("/me", response_model=UserDisplay, status_code=status.HTTP_200_OK)
async def read_users_me(
    current_user: Annotated[UserDisplay, Depends(get_current_user)]
):
    return current_user


# read one user
@router.get("/{id}", response_model=UserDisplay)
async def get_user(id: str, current_user: Annotated[User, Depends(get_current_user)]):
    if id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to access this resource.",
        )
    return current_user
