from fastapi import FastAPI
from app.db import models
from app.db.database import engine
from sqlalchemy.ext.asyncio import AsyncEngine
from app.router import user
import uvicorn
from app.config import settings

app = FastAPI()
app.include_router(user.router)


def start():
    uvicorn.run("app:main.app", port=settings.port, host="localhost")


async def create_tables(engine: AsyncEngine):
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


@app.on_event("startup")
async def startup_event():
    await create_tables(engine)
