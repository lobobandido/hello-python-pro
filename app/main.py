from fastapi import FastAPI
from typing import Dict

app = FastAPI(title="Hello Python Pro")

@app.get("/", response_model=Dict[str, str])
def read_root() -> Dict[str, str]:
    return {"message": "Hola, mundo desde FastAPI! vamos por todo"}
