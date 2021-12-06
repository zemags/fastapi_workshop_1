from db.models.arts import Art
from schemas.arts import ArtCreate
from sqlalchemy.orm import Session


def create_new_art(art: ArtCreate, db: Session, owner_id: int):
    art = Art(**art.dict(), owner_id=owner_id)
    db.add(art)
    db.commit()
    db.refresh(art)
    return art


def retreive_art(id: int, db: Session):
    art = db.query(Art).filter(Art.id == id).first()
    return art


def list_arts(db: Session):
    arts = db.query(Art).all()
    return arts


def update_art_by_id(id: int, art: ArtCreate, db: Session):
    existing_art = db.query(Art).filter(Art.id == id)
    if not existing_art.first():
        return 0
    existing_art.update(art.__dict__)
    db.commit()
    return 1
