from db.repository.owners import create_new_owner
from faker import Faker
from schemas.owners import OwnerCreate
from sqlalchemy.orm import Session

fake = Faker()


def create_random_owner(db: Session):
    ownername = fake.user_name()
    email = fake.ascii_email()
    password = fake.unix_time()
    owner_schema = OwnerCreate(ownername=ownername,
                               email=email, password=password)
    owner = create_new_owner(owner=owner_schema, db=db)
    return owner
