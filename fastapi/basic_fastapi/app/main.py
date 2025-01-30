from fastapi import FastAPI


# Create an entry point
app = FastAPI()


# Create and endpoint
@app.get("/")
def root():
    return {"status": "working..."}
