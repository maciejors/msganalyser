from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from backend.models.app_setup import ConfigurationModel, SetupSuccessRespose, IsDataLoadedResponse
from backend.models.common import BaseAppErrorModel
from backend.services.loading_data.read import (
    read_messenger_data, infer_data_owner,
)
from backend.services.loading_data.write import write_compact
from backend.services.loading_data.anonymiser import anonymise_data

router = APIRouter(
    prefix='/setup',
    tags=['setup'],
)


@router.put(
    '/',
    response_model=SetupSuccessRespose,
    responses={404: {
        'description': 'Data not found in the specified location',
        'model': BaseAppErrorModel,
    }},
)
async def setup(request: Request, config: ConfigurationModel):
    try:
        full_data_df = read_messenger_data(config.data_path)
        compact_save_location = ''
        if config.save_compact:
            compact_save_location = write_compact(full_data_df, config.data_path)
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
    return SetupSuccessRespose(data_owner=data_owner, path_to_compact=compact_save_location)


@router.get('/')
async def check_if_data_loaded(request: Request) -> IsDataLoadedResponse:
    return IsDataLoadedResponse(is_data_loaded=hasattr(request.app.state, 'data_df'))
