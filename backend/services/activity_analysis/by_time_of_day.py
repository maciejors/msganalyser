import pandas as pd


def msg_by_time_of_day(df: pd.DataFrame) -> pd.DataFrame:
    """
    Total number of messages by time of day (hour)
    """
    result = df[['hour', 'sender_name']] \
        .groupby('hour') \
        .count() \
        .reset_index() \
        .rename(columns={'hour': 'keys', 'sender_name': 'values'}) \
        .sort_values('keys')
    return result
