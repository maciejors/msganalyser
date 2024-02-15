from fastapi import APIRouter, Request

from backend.dependencies.errors import DataNotReadException
from backend.dependencies.filters import StandardFiltersAnnotated
from backend.dependencies.wrappers import functionality_wrapper
from backend.models.common import BaseAppErrorModel
from backend.models.analysis import Overview

from backend.services.overview import get_overview_df


router = APIRouter(
    prefix='/overview',
    tags=['overview'],
    responses={404: {
        'description': 'Data is yet to be read',
        'model': BaseAppErrorModel,
    }},
)


@router.get('/')
async def get_overview(request: Request, filters: StandardFiltersAnnotated) -> Overview:
    try:
        df = request.app.state.data_df
    except AttributeError:
        raise DataNotReadException()
    response = functionality_wrapper(get_overview_df, df, filters, Overview)
    return response
