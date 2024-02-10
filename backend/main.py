from fastapi import FastAPI

from backend.routers import chats, activity, app_setup

app = FastAPI(root_path='/api')
app.include_router(app_setup.router)
app.include_router(activity.router)
app.include_router(chats.router)
