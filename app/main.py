from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.routers import comment as comment_router
from app.routers import task as task_router
from app.routers import user as user_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router.router, prefix="/api", tags=["users"])
app.include_router(task_router.router, prefix="/api", tags=["tasks"])
app.include_router(comment_router.router, prefix="/api", tags=["comments"])


@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")
