from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from backend.models.app_setup import ConfigurationModel, DataOwnerModel
from backend.models.common import BaseAppErrorModel
from backend.services.reading_data.read import (
    read_messenger_data, infer_data_owner,
)
from backend.services.reading_data.anonymiser import anonymise_data
from backend.dependencies.errors import DataNotReadException

router = APIRouter(
    prefix='/setup',
    tags=['setup'],
)


@router.put(
    '/',
    response_model=DataOwnerModel,
    responses={404: {
        'description': 'Data not found in the specified location',
        'model': BaseAppErrorModel,
    }},
)
async def setup(request: Request, config: ConfigurationModel):
    try:
        full_data_df = read_messenger_data(config.data_path)
        full_data_df = anonymise_data(
            full_data_df,
            purge_contents=config.purge_contents,
            replace_names=config.replace_names,
        )
    except FileNotFoundError:
        return JSONResponse(
            status_code=404,
            content={'message': 'Facebook data not found in the specified location'}
        )
    data_owner = infer_data_owner(full_data_df)
    request.app.state.data_df = full_data_df
    request.app.state.data_owner = data_owner
    return DataOwnerModel(data_owner=data_owner)


@router.get(
    '/',
    responses={404: {
        'description': 'Data is yet to be read',
        'model': BaseAppErrorModel,
    }},
)
async def get_data_owner(request: Request) -> DataOwnerModel:
    try:
        return DataOwnerModel(data_owner=request.app.state.data_owner)
    except AttributeError:
        raise DataNotReadException()
