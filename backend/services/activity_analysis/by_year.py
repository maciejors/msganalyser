import pandas as pd


def msg_by_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Total number of messages by year
    """
    result = df[['year', 'sender_name']] \
        .groupby('year') \
        .count() \
        .reset_index() \
        .rename(columns={'year': 'datetime_key', 'sender_name': 'value'}) \
        .sort_values('datetime_key')
    return result
