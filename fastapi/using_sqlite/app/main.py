from datetime import datetime

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    time = datetime.now()
    return {
        "status": "working...",
        "time": time,
        "developed_by": "Felipe Silva",
    }
