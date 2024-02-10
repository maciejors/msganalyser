from fastapi import APIRouter, Request, HTTPException

from backend.models.app_setup import ConfigurationModel, DataOwnerModel
from backend.services.reading_data.read import (
    read_messenger_data, infer_data_owner,
)


router = APIRouter(
    prefix='/setup',
    tags=['setup'],
)


@router.put('/')
async def setup(request: Request, config: ConfigurationModel) -> DataOwnerModel:
    full_data_df = read_messenger_data(config.data_path, purge_contents=True)
    data_owner = infer_data_owner(full_data_df)
    request.app.state.data_df = full_data_df
    request.app.state.data_owner = data_owner
    return DataOwnerModel(data_owner=data_owner)


@router.get(
    '/', 
    responses={404: {'description': 'Data is yet to be read'}},
)
async def get_data_owner(request: Request) -> DataOwnerModel:
    try:
        return DataOwnerModel(data_owner=request.app.state.data_owner)
    except AttributeError:
        raise HTTPException(status_code=404, detail='Data is yet to be read')
