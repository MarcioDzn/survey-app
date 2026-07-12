from fastapi import FastAPI
from app.database import engine, Base

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}