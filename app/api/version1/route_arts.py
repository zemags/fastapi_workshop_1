from db.repository.arts import create_new_art
from db.session import get_db
from fastapi import APIRouter, Depends
from schemas.arts import ArtCreate, ShowArt
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/create-art", response_model=ShowArt)
def create_art(
    art: ArtCreate, db: Session = Depends(get_db)
):
    owner_id = 1
    art = create_new_art(art=art, db=db, owner_id=owner_id)
    return art
