import re

import pandas as pd


def __get_calls(df: pd.DataFrame, drop_unanswered=True) -> pd.DataFrame:
    df = df[df['@tags'].str.contains('@call')]
    if drop_unanswered:
        df = df[~df['@tags'].str.contains('<@call=0>')]
    return df


def top_calls_count(df: pd.DataFrame) -> pd.DataFrame:
    """
    The ranking of chats based on the number of calls
    """
    result = __get_calls(df) \
        .groupby('chat_name') \
        .count().reset_index() \
        .rename(columns={'sender_name': 'value'}) \
        .sort_values('value', ascending=False)
    return result[['chat_name', 'value']]


def top_calls_duration(df: pd.DataFrame) -> pd.DataFrame:
    """
    The ranking of chats based on the total duration of calls
    """
    calls_data = __get_calls(df)
    calls_durations_series = calls_data['@tags'].map(
        lambda tag_set: int(re.search(r'<@call=(\d+)>', tag_set).group(1))
    )
    result = calls_data \
        .assign(value=calls_durations_series) \
        .groupby('chat_name') \
        .sum() \
        .reset_index() \
        .sort_values('value', ascending=False)
    return result[['chat_name', 'value']]
