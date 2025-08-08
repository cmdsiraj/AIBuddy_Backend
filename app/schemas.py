from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class MessageOut(BaseModel):
    role: str
    content: str

    class Config:
        orm_mode = True

class MessageIn(BaseModel):
    message: str