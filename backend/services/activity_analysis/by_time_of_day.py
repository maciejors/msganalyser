import pandas as pd


def msg_by_time_of_day(df: pd.DataFrame) -> pd.DataFrame:
    """
    Total number of messages by time of day (hour)
    """
    result = df[['hour', 'sender_name']] \
        .groupby('hour') \
        .count() \
        .reset_index() \
        .rename(columns={'hour': 'datetime_key', 'sender_name': 'value'}) \
        .sort_values('datetime_key')
    result['datetime_key'] = result['datetime_key'].astype(str)
    return result
