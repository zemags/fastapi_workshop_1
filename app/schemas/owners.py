from pydantic import BaseModel, EmailStr


class OwnerCreate(BaseModel):
    ownername: str
    email: EmailStr
    password: str


class ShowOwner(BaseModel):
    # show exact fields in localhost/docs
    ownername: str
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True
