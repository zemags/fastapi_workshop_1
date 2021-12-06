from typing import List

from db.repository.arts import create_new_art, list_arts, retreive_art, \
    update_art_by_id, delete_art_by_id
from db.session import get_db
from fastapi import APIRouter, Depends, HTTPException
from schemas.arts import ArtCreate, ShowArt
from sqlalchemy.orm import Session
from starlette import status

router = APIRouter()


@router.post("/create-art", response_model=ShowArt)
def create_art(
    art: ArtCreate, db: Session = Depends(get_db)
):
    owner_id = 1
    art = create_new_art(art=art, db=db, owner_id=owner_id)
    return art


@router.get("/get/{id}", response_model=ShowArt)
def retreive_art_by_id(id: int, db: Session = Depends(get_db)):
    art = retreive_art(id=id, db=db)
    if not art:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Art {id} doesn't exist")
    return art


@router.get("/all", response_model=List[ShowArt])
def retreive_all_arts(db: Session = Depends(get_db)):
    arts = list_arts(db=db)
    return arts


@router.put("/update/{id}")
def update_art(id: int, art: ArtCreate, db: Session = Depends(get_db)):
    owner_id = 1
    art_retrieved = retreive_art(id=id, db=db)
    if not art_retrieved:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Art with {id} doesn't exist")
    update_art_by_id(id=id, art=art, db=db)
    return {"detail": "Successfully updated art"}


@router.delete("/delete/{id}")
def delete_art(id: int, db: Session = Depends(get_db)):
    art = retreive_art(id=id, db=db)
    if not art:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Art with {id} doesn't exist")
    delete_art_by_id(id=id, db=db)
    return {"detail": f"Successfully deleted art"}
