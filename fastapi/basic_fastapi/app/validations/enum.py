from enum import Enum

from fastapi import APIRouter


# instance the router
router = APIRouter()


# Example of using a path parameter with Enum
class ModelName(str, Enum):
    model1 = "model1"
    model2 = "model2"
    model3 = "model3"


@router.get("/models/{model_name}")
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
