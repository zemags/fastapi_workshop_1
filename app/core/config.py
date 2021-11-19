import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    # http://127.0.0.1:8000/docs
    PROJECT_TITLE: str = "App"
    PROJECT_VERSION: str = "0.1.1"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DB_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@" \
             f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()