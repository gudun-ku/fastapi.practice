from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello, World"}


@app.get("/blog/{id}")
def get_blog(id: int):
    return {"message": f"Blog with id: {id}"}


@app.post("/hello")
def hello():
    return "Hi!"
