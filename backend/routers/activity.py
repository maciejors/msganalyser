from fastapi import APIRouter, Request

from backend.dependencies.errors import DataNotReadException
from backend.dependencies.filters import StandardFiltersAnnotated
from backend.dependencies.wrappers import standard_functionality_wrapper
from backend.models.common import BaseAppErrorModel
from backend.models.analysis import DatetimeStat1D

from backend.services.activity_analysis.by_year import msg_by_year
from backend.services.activity_analysis.by_month import msg_by_month, avg_msg_by_calendar_month
from backend.services.activity_analysis.by_day import msg_by_day
from backend.services.activity_analysis.by_time_of_day import msg_by_time_of_day

router = APIRouter(
    prefix='/activity',
    tags=['activity'],
    responses={404: {
        'description': 'Data is yet to be read',
        'model': BaseAppErrorModel,
    }},
)


@router.get('/msg_by_year')
async def get_msg_by_year(request: Request, filters: StandardFiltersAnnotated) -> DatetimeStat1D:
    try:
        df = request.app.state.data_df
    except AttributeError:
        raise DataNotReadException()
    response = standard_functionality_wrapper(msg_by_year, df, filters, DatetimeStat1D)
    return response


@router.get('/msg_by_month')
async def get_msg_by_month(request: Request, filters: StandardFiltersAnnotated) -> DatetimeStat1D:
    try:
        df = request.app.state.data_df
    except AttributeError:
        raise DataNotReadException()
    response = standard_functionality_wrapper(msg_by_month, df, filters, DatetimeStat1D)
    return response


@router.get('/avg_msg_by_calendar_month')
async def get_avg_msg_by_calendar_month(request: Request,
                                        filters: StandardFiltersAnnotated) -> DatetimeStat1D:
    try:
        df = request.app.state.data_df
    except AttributeError:
        raise DataNotReadException()
    response = standard_functionality_wrapper(avg_msg_by_calendar_month, df, filters, DatetimeStat1D)
    return response


@router.get('/msg_by_day')
async def get_msg_by_day(request: Request, filters: StandardFiltersAnnotated) -> DatetimeStat1D:
    try:
        df = request.app.state.data_df
    except AttributeError:
        raise DataNotReadException()
    response = standard_functionality_wrapper(msg_by_day, df, filters, DatetimeStat1D)
    return response


@router.get('/msg_by_time_of_day')
async def get_msg_by_time_of_day(request: Request, filters: StandardFiltersAnnotated) -> DatetimeStat1D:
    try:
        df = request.app.state.data_df
    except AttributeError:
        raise DataNotReadException()
    response = standard_functionality_wrapper(msg_by_time_of_day, df, filters, DatetimeStat1D)
    return response
