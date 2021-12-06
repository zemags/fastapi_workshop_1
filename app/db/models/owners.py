from db.base_class import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship


class Owner(Base):
    id = Column(Integer, primary_key=True, index=True)
    ownername = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=False)
    is_superuser = Column(Boolean(), default=False)
    arts = relationship("Art", back_populates="owner")
