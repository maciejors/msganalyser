import pandas as pd

from ..utils.datetimefunc import (
    get_sortable_month_str_from_timestamp,
    get_pretty_month_str_from_sortable,
)


def msg_by_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Total number of messages by month
    """
    pretty_month_series = df['timestamp_ms'] \
        .map(get_sortable_month_str_from_timestamp) \
        .map(get_pretty_month_str_from_sortable)
    result = df.assign(key=pretty_month_series) \
        .groupby(['year', 'month', 'key']) \
        .count() \
        .reset_index() \
        .sort_values(['year', 'month']) \
        [['key', 'sender_name']] \
        .rename(columns={'sender_name': 'value'})
    return result


def avg_msg_by_calendar_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Average number of messages by calendar month
    """
    avg_by_month = df.groupby(['year', 'month']) \
        .count() \
        .groupby('month') \
        .mean() \
        .reset_index()
    avg_by_month['value'] = avg_by_month['sender_name'] \
        .round(0) \
        .astype(int)
    result = avg_by_month[['month', 'value']] \
        .rename(columns={'month': 'key'})
    return result
