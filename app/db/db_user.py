from app.db.hash import Hash
from sqlalchemy import select
from app.schemas import UserBase
from app.db.models import User
from fastapi import HTTPException, status
from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession


async def create_user(db: AsyncSession, request: UserBase):
    new_user = User(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


async def get_all_users(db: AsyncSession) -> Sequence[User]:
    result = await db.execute(select(User))
    users: Sequence[User] = result.scalars().all()
    return users


async def get_user(db: AsyncSession, id: int) -> User:
    # handle any exceptions
    result = await db.execute(select(User).where(User.id == id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )
    return user


async def update_user(db: AsyncSession, id: int, request: UserBase):
    user: User = await get_user(db, id)
    user.update(
        {
            User.username: request.username,
            User.email: request.email,
            User.password: Hash.bcrypt(request.password),
        }
    )

    await db.commit()
    return "ok"


async def delete_user(db: AsyncSession, id: int):
    user: User = await get_user(db, id)
    # handle any exception

    await db.delete(user)
    await db.commit()
    return "ok"
