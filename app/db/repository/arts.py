from db.models.arts import Art
from schemas.arts import ArtCreate
from sqlalchemy.orm import Session


def create_new_art(art: ArtCreate, db: Session, owner_id: int):
    art = Art(**art.dict(), owner_id=owner_id)
    db.add(art)
    db.commit()
    db.refresh(art)
    return art
