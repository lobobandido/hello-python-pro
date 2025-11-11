from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    environment: str = "development"
    database_url: str = "sqlite:///./database.db"
    project_name: str = "Hello Python Pro"

    class Config:
        env_file = ".env"


settings = Settings()
