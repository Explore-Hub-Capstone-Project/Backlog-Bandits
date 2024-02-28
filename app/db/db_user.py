from fastapi import HTTPException, status
from pymongo.database import Database
from pymongo.collection import Collection
from bson.objectid import ObjectId
from datetime import datetime
from app.db.hash import Hash
from app.schemas import UserCreate, UserGet, User
from app import jwttoken
from typing import Any


async def get_user_by_id(db: Database, id: int):
    user_collection = db.get_collection("users")
    user = user_collection.find_one({"id": id})

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return user


async def get_user(db: Database, request: UserGet):
    if request.id:
        user_identifier = {"_id": ObjectId(request.id)}
    elif request.email:
        user_identifier = {"email": request.email}
    elif request.username:
        user_identifier = {"username": request.username}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    print("User identifier:", user_identifier)
    collection: Collection[dict[str, Any]] = db.get_collection("users")
    user = collection.find_one(user_identifier)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    user["id"] = str(user.pop("_id"))
    return User(**user)


async def create_user(db: Database, request: UserCreate):
    collection = db.get_collection("users")
    existing_user = collection.find_one({"email": request.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = Hash.bcrypt(request.password)
    existing_username = collection.find_one({"username": request.username})
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already exists.")

    user = {
        "firstname": request.firstname,
        "lastname": request.lastname,
        "username": request.username,
        "email": request.email,
        "mobile": request.mobile,
        "country": request.country,
        "password": hashed_password,
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow(),
    }

    result = collection.insert_one(user)
    if not result.acknowledged:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="User could not be created due to an error.",
        )

    user["id"] = str(result.inserted_id)
    print(user)
    return user


async def authenticate_user(db: Database, identifier: UserGet, password: str):
    collection: Collection[dict[str, Any]] = db.get_collection("users")
    if identifier.id:
        query = {"_id": ObjectId(identifier.id)}
    elif identifier.email:
        query = {"email": identifier.email}
    elif identifier.username:
        query = {"username": identifier.username}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    user = collection.find_one(query)

    if user and Hash.verify(user["password"], password):
        access_token = jwttoken.create_access_token(
            data={"user_email": user["email"], "user_id": str(user["_id"])}
        )
        user["id"] = str(user.pop("_id"))
        return {"user": user, "access_token": access_token, "token_type": "bearer"}

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="User is not authorized",
    )


async def update_user_info(db: Database, email: str, update_data: dict):
    collection = db.get_collection("users")
    if "password" in update_data:
        update_data["password"] = Hash.bcrypt(update_data["password"])
    update_data["updatedAt"] = datetime.utcnow()
    result = collection.update_one({"email": email}, {"$set": update_data})
    if result.modified_count == 0:
        return None
    return update_data
