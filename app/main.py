from fastapi import FastAPI

# from app.db.database import engine
from app.router import user
import uvicorn
from app.config import settings
from fastapi.middleware.cors import CORSMiddleware


origins = ["http://localhost:3000"]


app = FastAPI()
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
