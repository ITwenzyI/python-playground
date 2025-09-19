from fastapi import APIRouter
from typing import Optional

router = APIRouter()

@router.get("/hello")
def hello_world():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
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