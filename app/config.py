from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    port: int = 5000
    db_username: str = "postgres"
    db_password: str = "postgres"
    db_host: str = "localhost"
    db_database: str = "explorehub"


settings = Settings()
