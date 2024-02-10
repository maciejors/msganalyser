from fastapi import FastAPI

from .routers import chats, activity, app_setup

app = FastAPI()
app.include_router(app_setup.router)
app.include_router(activity.router)
app.include_router(chats.router)
