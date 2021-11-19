from pydantic import BaseModel, EmailStr


class OwnerCreate(BaseModel):
    username: str
    email: EmailStr
    password: str