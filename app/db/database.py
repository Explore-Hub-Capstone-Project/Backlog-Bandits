from pymongo import MongoClient
from typing import Dict, Any
from app.config import settings


def get_db():
    client: MongoClient[Dict[str, Any]] = MongoClient(
        settings.connection_string, settings.mongo_port
    )
    db = client[settings.database_name]

    try:
        yield db

    finally:
        client.close()
