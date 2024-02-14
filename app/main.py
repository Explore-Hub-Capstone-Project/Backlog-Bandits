from fastapi import FastAPI
from app.db import models
from app.db.database import engine
from sqlalchemy.ext.asyncio import AsyncEngine
from contextlib import asynccontextmanager
from app.router import user
import uvicorn
from app.config import settings
from fastapi.middleware.cors import CORSMiddleware


origins = ["http://localhost:3000"]


async def create_tables(asyncEngine: AsyncEngine):
    async with asyncEngine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables(engine)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(user.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


def start():
    uvicorn.run(
        "app.main:app",
        host="localhost",
        port=settings.port,
        reload=False,
    )


if __name__ == "__main__":
    start()
