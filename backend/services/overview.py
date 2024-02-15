import pandas as pd

from .chats_rankings.calls import top_calls_count, top_calls_duration
from .chats_rankings.counting_messages import top_media_count, top_msg_count
from .activity_analysis import msg_by_day


def get_overview_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns general statistics
    """
    msg_count = len(df)
    calls_count = top_calls_count(df).sum()['value']
    calls_duration = top_calls_duration(df).sum()['value']
    media_count = top_media_count(df).sum()['value']
    favourite_chat = top_msg_count(df).iloc[0]['chat_name'] if msg_count > 0 else 'N/A'
    if msg_count == 0:
        most_active_day = 'N/A'
    else:
        activity_by_day = msg_by_day(df)
        most_active_day = activity_by_day[activity_by_day['value'] == activity_by_day['value'].max()]\
            .iloc[0]['datetime_key']
    return pd.DataFrame(dict(
        total_msg_count=[msg_count],
        total_calls_count=[calls_count],
        total_calls_duration_s=[calls_duration],
        total_media_count=[media_count],
        favourite_chat=[favourite_chat],
        most_active_day=[most_active_day],
    ))
