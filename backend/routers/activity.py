from fastapi import APIRouter, Request

from backend.dependencies.filters import StandardFiltersAnnotated
from backend.dependencies.wrappers import standard_functionality_wrapper
from backend.models.analysis import TwoDimensionalData
from backend.services.activity_analysis.by_year import msg_per_year

router = APIRouter(
    prefix='/activity',
    tags=['activity'],
)


@router.get('/msg_per_year')
async def get_msg_per_year(request: Request, filters: StandardFiltersAnnotated) -> TwoDimensionalData:
    df = request.app.state.data_df
    response = standard_functionality_wrapper(msg_per_year, df, filters)
    return response
