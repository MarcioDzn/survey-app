from fastapi import FastAPI

from app.routes import survey_router, user_router

app = FastAPI()

app.include_router(user_router)
app.include_router(survey_router)


@app.get("/")
def home():
    return {"message": "Hello World"}
