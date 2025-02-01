from datetime import datetime
from fastapi import FastAPI
from parameters import path_parameters, query_parameters
from validations import enum
from bodyrequest import body_request


# set the entry point
app = FastAPI()

# include routes
app.include_router(path_parameters.router, prefix=("/pathparams"))
app.include_router(query_parameters.router, prefix=("/queryparams"))
app.include_router(enum.router, prefix=("/validation"))
app.include_router(body_request.router, prefix=("/body_request"))


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
