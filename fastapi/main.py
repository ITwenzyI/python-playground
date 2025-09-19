from fastapi import FastAPI
from typing import List
from fastapi import Query

from routers import hello
from routers import status

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}

@app.get("/tags")
def get_tags(tag: List[str] = Query([])):
    return {"tags": tag}

app.include_router(hello.router)

app.include_router(status.router)