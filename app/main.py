from fastapi import FastAPI

app = FastAPI(title="FastAPI Notes")

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI Notes!"}
