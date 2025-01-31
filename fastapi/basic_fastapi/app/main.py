from datetime import datetime
from typing import Optional
from enum import Enum

from fastapi import FastAPI, Request
from pydantic import BaseModel


# set the entry point
app = FastAPI()


# Create a class based on the BaseModel from pydantic
class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


# set initial end point
@app.get("/")
def root():
    time = datetime.now()
    return {
        "project name": "Initial FastAPI",
        "greeting": "Hello this is my first project using fastapi",
        "working at": time,
        "developed by": "Felipe Silva",
    }


# Get endpoint with a path parameter and a query parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


# Set a put endpoint
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


# Example of using a path parameter with Enum
class ModelName(str, Enum):
    model1 = "model1"
    model2 = "model2"
    model3 = "model3"


@app.get("/models/{model_name}")
def model(model_name: ModelName):
    if model_name is ModelName.model1:
        return {
            "model_name": model_name,
            "model_type": "The type is the model 1",
        }

    if model_name is ModelName.model2:
        return {
            "model_name": model_name,
            "model_type": "This is the model 2 you have luck",
        }

    return {
        "model_name": model_name,
        "model_type": "There is no model to show",
    }


# Multiple query parameters
@app.get("/queries")
def queries(request: Request):
    params = dict(request.query_params)
    return {"Query params": params}
