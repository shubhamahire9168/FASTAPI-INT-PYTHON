from jose import jwt, JWTError

SECRET_KEY = "mysecret"
ALGORITHM = "HS256"


def create_token(data: dict):

    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return token


def verify_token(token: str):

    try:

        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        return data

    except JWTError:

        return None