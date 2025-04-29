import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    rpc_url: str
    wallet_address: str
    wallet_private_key: str
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()
