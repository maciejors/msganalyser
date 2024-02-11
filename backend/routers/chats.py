from fastapi import APIRouter, Request

from backend.dependencies.errors import DataNotReadException
from backend.dependencies.filters import StandardFiltersAnnotated
from backend.dependencies.wrappers import functionality_wrapper
from backend.models.common import BaseAppErrorModel
from backend.models.analysis import DateChatStat, ChatStat, ChatStreakStat

from backend.services.chats_rankings.top_chats_by_date import (
    top_chats_by_year, top_chats_by_month, top_chats_by_day, chat_of_the_day_counts,
)
from backend.services.chats_rankings.counting_messages import (
    top_msg_count, top_media_count,
)
from backend.services.chats_rankings.calls import (
    top_calls_count, top_calls_duration,
)
from backend.services.chats_rankings.counting_days import (
    days_with_msg_count, longest_streaks,
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


@router.get('/chat_of_the_day_counts')
async def get_chat_of_the_day_counts(request: Request, filters: StandardFiltersAnnotated) -> ChatStat:
    try:
        df = request.app.state.data_df
    except AttributeError:
        raise DataNotReadException()
    response = functionality_wrapper(chat_of_the_day_counts, df, filters, ChatStat)
    return response


@router.get('/top_msg_count')
async def get_top_msg_count(request: Request, filters: StandardFiltersAnnotated) -> ChatStat:
    try:
        df = request.app.state.data_df
    except AttributeError:
        raise DataNotReadException()
    response = functionality_wrapper(top_msg_count, df, filters, ChatStat)
    return response


@router.get('/top_media_count')
async def get_top_media_count(request: Request, filters: StandardFiltersAnnotated) -> ChatStat:
    try:
        df = request.app.state.data_df
    except AttributeError:
        raise DataNotReadException()
    response = functionality_wrapper(top_media_count, df, filters, ChatStat)
    return response


@router.get('/top_calls_count')
async def get_top_calls_count(request: Request, filters: StandardFiltersAnnotated) -> ChatStat:
    try:
        df = request.app.state.data_df
    except AttributeError:
        raise DataNotReadException()
    response = functionality_wrapper(top_calls_count, df, filters, ChatStat)
    return response


@router.get('/top_calls_duration')
async def get_top_calls_duration(request: Request, filters: StandardFiltersAnnotated) -> ChatStat:
    try:
        df = request.app.state.data_df
    except AttributeError:
        raise DataNotReadException()
    response = functionality_wrapper(top_calls_duration, df, filters, ChatStat)
    return response


@router.get('/days_with_msg_count')
async def get_days_with_msg_count(request: Request, filters: StandardFiltersAnnotated) -> ChatStat:
    try:
        df = request.app.state.data_df
    except AttributeError:
        raise DataNotReadException()
    response = functionality_wrapper(days_with_msg_count, df, filters, ChatStat)
    return response


@router.get('/longest_streaks')
async def get_longest_streaks(request: Request, filters: StandardFiltersAnnotated) -> ChatStreakStat:
    try:
        df = request.app.state.data_df
    except AttributeError:
        raise DataNotReadException()
    response = functionality_wrapper(longest_streaks, df, filters, ChatStreakStat)
    return response
