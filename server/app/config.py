from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str

    class Config:
        env_file = ".env"

settings = Settings() # type: ignore #getting "Arguments missing for parameters "database_url", "secret_key""