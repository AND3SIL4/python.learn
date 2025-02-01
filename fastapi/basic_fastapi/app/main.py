from datetime import datetime
from fastapi import FastAPI


# set the entry point
app = FastAPI()


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
