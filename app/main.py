from fastapi import FastAPI
from app.routes import user, auth_routes
from app.database import engine
from app import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(user.router)
app.include_router(auth_routes.router)


@app.get("/", tags=["Home-Api"])
def home():
    return {"msg": "FAST-APi integration Running Successfully"}

