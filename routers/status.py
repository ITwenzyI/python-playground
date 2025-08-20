from fastapi import APIRouter
from typing import Optional

router = APIRouter()

@router.get("/status")
def get_status(status: Optional[str] = "ok"):
    return {"status": status}