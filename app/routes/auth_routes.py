from fastapi import APIRouter, HTTPException, Header
from app.schemas import Login
from app.auth import create_token, verify_token

router = APIRouter()

users = []


@router.post("/register", tags=["Auth"])
def register(user: Login):

    users.append(user.dict())

    return {"msg": "user created"}


@router.post("/login", tags=["Auth"])
def login(user: Login):

    for u in users:

        if u["username"] == user.username and u["password"] == user.password:

            token = create_token({"username": u["username"]})

            return {"token": token}

    raise HTTPException(status_code=401, detail="Invalid user")


@router.get("/profile", tags=["Auth"])
def profile(token: str = Header()):

    data = verify_token(token)

    if not data:
        raise HTTPException(status_code=401, detail="Invalid token")

    return data