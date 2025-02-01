from typing import Optional, List

from fastapi import APIRouter, Request


# instance the api router
router = APIRouter()


# Get endpoint with a path parameter and a query parameter
@router.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


# Multiple query parameters
@router.get("/queries")
def queries(request: Request):
    params = dict(request.query_params)
    return {"Query params": params}


# Working with query parameters
fake_db: List[str] = [
    {"item_name": "apple"},
    {"item_name": "banana"},
    {"item_name": "orange"},
]


@router.get("/items_by_name")
async def items_name(skip: int = 0, limit: int = 10):
    return fake_db[skip: limit + skip]
