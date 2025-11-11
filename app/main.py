from fastapi import FastAPI

from app.db import create_db_and_tables
from app.routes.users import router as users_router

app = FastAPI(title="Hello Python Pro")


@app.on_event("startup")
def on_startup() -> None:
    create_db_and_tables()


app.include_router(users_router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hola, mundo desde FastAPI! vamos por todo"}
