from db.repository.owners import create_new_owner
from db.session import get_db
from fastapi import APIRouter, Depends
from schemas.owners import OwnerCreate, ShowOwner
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=ShowOwner)
def create_owner(owner: OwnerCreate, db: Session = Depends(get_db)):
    owner = create_new_owner(owner, db)
    return owner
