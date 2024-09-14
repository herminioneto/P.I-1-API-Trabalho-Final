from fastapi import FastAPI
from routes import task

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKsefudemomt"}
from fastapi import FastAPI


app.include_router(task.router)
