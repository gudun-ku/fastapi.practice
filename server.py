from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello, World"}


@app.post("/hello")
def hello():
    return "Hi!"