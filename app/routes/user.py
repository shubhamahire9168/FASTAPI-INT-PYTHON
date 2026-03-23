from fastapi import APIRouter
from app.schemas import User, UserCreate
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import models
from app.security import hash_password

router = APIRouter()

users = []


@router.get("/users", tags=["Users"])
def get_users():
    return users


@router.post("/user", tags=["Users"])
def create_user(user: User):
    users.append(user.dict())
    return users


@router.get("/user/{index}", tags=["Users"])
def get_user(index: int):

    if index >= len(users):
        return {"error": "User not found"}

    return users[index]


@router.put("/user/{index}", tags=["Users"])
def update_user(index: int, user: User):

    if index >= len(users):
        return {"error": "User not found"}

    users[index] = user.dict()

    return users


@router.delete("/user/{index}", tags=["Users"])
def delete_user(index: int):

    if index >= len(users):
        return {"error": "User not found"}

    users.pop(index)

    return users

# ================= DB APIs =================


@router.post("/db/user", tags=["DB Users"])
@router.post("/db/user", tags=["DB Users"])
def create_user_db(user: UserCreate, db: Session = Depends(get_db)):

    new_user = models.User(
        name=user.name,
        age=user.age,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/db/users", tags=["DB Users"])
def get_users_db(db: Session = Depends(get_db)):

    users = db.query(models.User).all()

    return users


@router.get("/db/user/{id}", tags=["DB Users"])
def get_user_db(id: int, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        return {"error": "User not found"}

    return user


@router.put("/db/user/{id}", tags=["DB Users"])
def update_user_db(id: int, user: User, db: Session = Depends(get_db)):

    db_user = db.query(models.User).filter(models.User.id == id).first()

    if not db_user:
        return {"error": "User not found"}

    db_user.name = user.name
    db_user.age = user.age

    db.commit()

    return db_user


@router.delete("/db/user/{id}", tags=["DB Users"])
def delete_user_db(id: int, db: Session = Depends(get_db)):

    db_user = db.query(models.User).filter(models.User.id == id).first()

    if not db_user:
        return {"error": "User not found"}

    db.delete(db_user)
    db.commit()

    return {"msg": "User deleted"}

    