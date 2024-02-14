from sqlalchemy import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)
from app.config import settings


uri = URL.create(
    "postgresql+asyncpg",
    username=settings.db_username,
    password=settings.db_password,  # plain (unescaped) text
    host=settings.db_host,
    database=settings.db_database,
)

engine = create_async_engine(uri, future=True, echo=True)
Session = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


async def get_db():
    db = Session()
    try:
        yield db

    finally:
        await db.close()
