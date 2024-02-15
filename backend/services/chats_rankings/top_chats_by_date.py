import pandas as pd

from ..utils.datetimefunc import (
    get_sortable_month_str_from_timestamp,
    get_pretty_month_str_from_sortable,
    get_sortable_day_str_from_timestamp,
    get_pretty_day_str_from_sortable,
)


def top_chats_by_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Chats with the most messages by year
    """
    yearly_counts_chats = df[['year', 'chat_name', 'sender_name']] \
        .groupby(['year', 'chat_name']) \
        .count() \
        .reset_index() \
        .rename(columns={'sender_name': 'value'})
    result = yearly_counts_chats \
        .loc[yearly_counts_chats.groupby(['year'])['value'].idxmax()] \
        .rename(columns={'year': 'datetime_key'}) \
        .sort_values('datetime_key', ascending=False)
    result['datetime_key'] = result['datetime_key'].astype(str)
    return result


def top_chats_by_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Chats with the most messages by month
    """
    pretty_month_series = df['timestamp_ms'] \
        .map(get_sortable_month_str_from_timestamp) \
        .map(get_pretty_month_str_from_sortable)
    monthly_counts_chats = df.assign(datetime_key=pretty_month_series) \
        .groupby(['year', 'month', 'datetime_key', 'chat_name']) \
        .count() \
        .reset_index() \
        .rename(columns={'sender_name': 'value'})
    result = monthly_counts_chats \
        .loc[monthly_counts_chats.groupby(['datetime_key'])['value'].idxmax()] \
        .sort_values(['year', 'month'], ascending=False)
    return result[['datetime_key', 'chat_name', 'value']]


def top_chats_by_day(df: pd.DataFrame) -> pd.DataFrame:
    """
    Chats with the most messages by day
    """
    pretty_day_series = df['timestamp_ms'] \
        .map(get_sortable_day_str_from_timestamp) \
        .map(get_pretty_day_str_from_sortable)
    daily_counts_chats = df.assign(datetime_key=pretty_day_series) \
        .groupby(['year', 'month', 'day', 'datetime_key', 'chat_name']) \
        .count() \
        .reset_index() \
        .rename(columns={'sender_name': 'value'})
    result = daily_counts_chats \
        .loc[daily_counts_chats.groupby(['datetime_key'])['value'].idxmax()] \
        .sort_values(['year', 'month', 'day'], ascending=False)
    return result[['datetime_key', 'chat_name', 'value']]


def chat_of_the_day_counts(df: pd.DataFrame) -> pd.DataFrame:
    """
    How many times each chat was the chat of the day, i.e. had the most
    messages of all chats on a day.
    """
    result = top_chats_by_day(df) \
        .groupby('chat_name') \
        .count() \
        .reset_index() \
        .sort_values('value', ascending=False)
    return result[['chat_name', 'value']]


def chat_of_the_month_counts(df: pd.DataFrame) -> pd.DataFrame:
    """
    How many times each chat was the chat of the month, i.e. had the most
    messages of all chats in a month.
    """
    result = top_chats_by_month(df) \
        .groupby('chat_name') \
        .count() \
        .reset_index() \
        .sort_values('value', ascending=False)
    return result[['chat_name', 'value']]
