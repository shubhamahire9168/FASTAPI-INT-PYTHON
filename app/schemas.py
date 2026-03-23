from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


class Login(BaseModel):
    username: str
    password: str


class UserCreate(BaseModel):
    name: str
    age: int
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    age: int

    class Config:
        from_attributes = True


