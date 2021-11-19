from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

DB_URI = settings.DB_URI
engine = create_engine(DB_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    # for dependency injection
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()