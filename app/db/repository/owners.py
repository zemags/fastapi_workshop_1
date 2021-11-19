from core.hashing import Hasher
from db.models.owners import Owner
from schemas.owners import OwnerCreate
from sqlalchemy.orm import Session


def create_new_owner(owner: OwnerCreate, db: Session):
    owner = Owner(ownername=owner.ownername,
                  email=owner.email,
                  hashed_password=Hasher.get_password_hash(owner.password),
                  is_active=True,
                  is_superuser=False)
    db.add(owner)
    db.commit()
    db.refresh(owner)
    return owner
