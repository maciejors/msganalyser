from fastapi import FastAPI
from fastapi.responses import JSONResponse

from backend.routers import chats, activity, app_setup
from backend.dependencies.errors import DataNotReadException


app = FastAPI(root_path='/api')
app.include_router(app_setup.router)
app.include_router(activity.router)
app.include_router(chats.router)


@app.exception_handler(DataNotReadException)
async def data_not_read_exception_handler():
    return JSONResponse(
        status_code=404,
        content={'message': 'Data is yet to be read'}
    )
