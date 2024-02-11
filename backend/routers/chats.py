from fastapi import APIRouter, Request

from backend.dependencies.errors import DataNotReadException
from backend.dependencies.filters import StandardFiltersAnnotated
from backend.dependencies.wrappers import functionality_wrapper
from backend.models.common import BaseAppErrorModel
from backend.models.analysis import DateChatStat

from backend.services.chats_rankings.top_chats_by_date import (
    top_chats_by_year, top_chats_by_month, top_chats_by_day,
)


router = APIRouter(
    prefix='/chats',
    tags=['chats'],
    responses={404: {
        'description': 'Data is yet to be read',
        'model': BaseAppErrorModel,
    }},
)


@router.get('/top_chats_by_year')
async def get_top_chats_by_year(request: Request, filters: StandardFiltersAnnotated) -> DateChatStat:
    try:
        df = request.app.state.data_df
    except AttributeError:
        raise DataNotReadException()
    response = functionality_wrapper(top_chats_by_year, df, filters, DateChatStat)
    return response


@router.get('/top_chats_by_month')
async def get_top_chats_by_month(request: Request, filters: StandardFiltersAnnotated) -> DateChatStat:
    try:
        df = request.app.state.data_df
    except AttributeError:
        raise DataNotReadException()
    response = functionality_wrapper(top_chats_by_month, df, filters, DateChatStat)
    return response


@router.get('/top_chats_by_day')
async def get_top_chats_by_day(request: Request, filters: StandardFiltersAnnotated) -> DateChatStat:
    try:
        df = request.app.state.data_df
    except AttributeError:
        raise DataNotReadException()
    response = functionality_wrapper(top_chats_by_day, df, filters, DateChatStat)
    return response
