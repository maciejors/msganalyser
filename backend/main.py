from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from backend.routers import chats, activity, app_setup, overview
from backend.dependencies.errors import DataNotReadException


app = FastAPI(root_path='/api')

origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(app_setup.router)
app.include_router(overview.router)
app.include_router(activity.router)
app.include_router(chats.router)


@app.exception_handler(DataNotReadException)
async def data_not_read_exception_handler(request: Request, exc: DataNotReadException):
    return JSONResponse(
        status_code=404,
        content={'message': 'Data is yet to be read'}
    )
