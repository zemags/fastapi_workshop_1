from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel


class ArtBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()


class ArtCreate(ArtBase):
    title: str
    description: str


class ShowArt(ArtBase):
    title: str
    description: str
    date_posted: date

    class Config():
        orm_mode = True
