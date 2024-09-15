from fastapi import FastAPI

from app.routers import task as task_router
from app.routers import user as user_router

app = FastAPI()

app.include_router(user_router.router, prefix="/api", tags=["users"])
app.include_router(task_router.router, prefix="/api", tags=["tasks"])


@app.get("/")
def read_root():
    return {"message": "Hello World"}
