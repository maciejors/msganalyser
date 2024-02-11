import pandas as pd

from ..utils.datetimefunc import (
    get_sortable_day_str_from_timestamp,
    get_pretty_day_str_from_sortable,
)


def msg_by_day(df: pd.DataFrame) -> pd.DataFrame:
    """
    Total number of messages by day
    """
    pretty_day_series = df['timestamp_ms'] \
        .map(get_sortable_day_str_from_timestamp) \
        .map(get_pretty_day_str_from_sortable)
    result = df.assign(keys=pretty_day_series) \
        .groupby(['year', 'month', 'day', 'keys']) \
        .count() \
        .reset_index() \
        .sort_values(['year', 'month', 'day']) \
        [['keys', 'sender_name']] \
        .rename(columns={'sender_name': 'values'})
    return result
