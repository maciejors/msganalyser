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
        .rename(columns={'year': 'key'}) \
        .sort_values('key')
    return result


def top_chats_by_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Chats with the most messages by month
    """
    pretty_month_series = df['timestamp_ms'] \
        .map(get_sortable_month_str_from_timestamp) \
        .map(get_pretty_month_str_from_sortable)
    monthly_counts_chats = df.assign(key=pretty_month_series) \
        .groupby(['year', 'month', 'key', 'chat_name']) \
        .count() \
        .reset_index() \
        .rename(columns={'sender_name': 'value'})
    result = monthly_counts_chats \
        .loc[monthly_counts_chats.groupby(['key'])['value'].idxmax()] \
        .sort_values(['year', 'month']) \
        [['key', 'chat_name', 'value']]
    return result


def top_chats_by_day(df: pd.DataFrame) -> pd.DataFrame:
    """
    Chats with the most messages by day
    """
    pretty_day_series = df['timestamp_ms'] \
        .map(get_sortable_day_str_from_timestamp) \
        .map(get_pretty_day_str_from_sortable)
    daily_counts_chats = df.assign(key=pretty_day_series) \
        .groupby(['year', 'month', 'day', 'key', 'chat_name']) \
        .count() \
        .reset_index() \
        .rename(columns={'sender_name': 'value'})
    result = daily_counts_chats \
        .loc[daily_counts_chats.groupby(['key'])['value'].idxmax()] \
        .sort_values(['year', 'month', 'day']) \
        [['key', 'chat_name', 'value']]
    return result
