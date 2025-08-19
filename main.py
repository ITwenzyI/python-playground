from fastapi import FastAPI
from typing import Optional
from typing import List
from fastapi import Query

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}

@app.get("/hello/{name}")
def hello_name(name: str,
               lang: Optional[str] = None,
               upper: Optional[bool] = False,
               style: Optional[str] = "casual",
               times: Optional[int] = 1
               ):
    if lang == "de":
        if style == "formal":
            message = f"Guten Tag {name}"
        else:
            message = f"Hallo {name}"
    elif lang == "en":
        message = f"Hello {name}"
    elif lang == "fr":
        message = f"Bonjour {name}"
    else:
        message = f"Hello {name}"

    if upper:
        message = message.upper()

    # messages = []
    # for _ in range(times):
    #     messages.append(message)
    messages = [message for _ in range(times)]

    return {"message": messages}

@app.get("/tags")
def get_tags(tag: List[str] = Query([])):
    return {"tags": tag}