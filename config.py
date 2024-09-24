import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
load_dotenv()

class Settings(BaseSettings):
    POSTGRES_USER: str=os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str=os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str=os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT: str=os.getenv("POSTGRES_PORT","5432")
    POSTGRES_DB: str=os.getenv("POSTGRES_DB")
    DATABASE_URL: str=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    S3_BUCKET: str=os.getenv("S3_BUCKET")
settings=Settings()