from typing import Optional

from fastapi import APIRouter

router = APIRouter()


# With optional query parameters
@router.get("/optional/{item_id}")
async def optional(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "query": q}
    else:
        return {"item_id": item_id}


# type convert
@router.get("/convert/{item_id}")
async def convert(item_id: str, q: str | None = None, short: bool = True):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# No order specific for query parameters
@router.get("/users/{user_id}/items/{item_id}")
def noorder(
    user_id: int,
    item_id: int,
    required: str,
    q: Optional[str] = None,
    short: bool = False,
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"query_param": q})
    if not short:
        item.update({"description": "Long description"})
    return item
