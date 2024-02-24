from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    port: int = 5000
    mongo_port: int = 27017
    connection_string: str = "mongodb://localhost"
    database_name: str = "ExploreHub-DB"


settings = Settings()
