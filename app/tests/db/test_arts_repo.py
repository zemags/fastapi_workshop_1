from db.repository.arts import create_new_art
from db.repository.arts import retreive_art
from schemas.arts import ArtCreate
from sqlalchemy.orm import Session
from tests.utils.users import create_random_owner


def test_retreive_art_by_id(db_session: Session):
    title = "test title"
    description = "test description"
    owner = create_random_owner(db=db_session)
    art_schema = ArtCreate(title=title, description=description)
    art = create_new_art(art=art_schema, db=db_session, owner_id=owner.id)
    retreived_art = retreive_art(id=art.id, db=db_session)
    assert retreived_art.id == art.id
    assert retreived_art.title == "test title"
