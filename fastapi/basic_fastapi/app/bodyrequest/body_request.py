from fastapi import APIRouter
from pydantic import BaseModel


# instance the router
router = APIRouter()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@router.post("/set_item")
async def set_item(item: Item):
    item_dict = item.dict()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# request body with path parameter
@router.post("/items/{item_id}")
async def another(item: Item, item_id: int):
    return {"item_id": item_id, **item.dict()}


# Request body + path parameter + query parameter
@router.post("/request/{item_id}")
async def request(item: Item, item_id: int, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"query_param": q})
    return result
