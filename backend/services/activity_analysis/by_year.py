import pandas as pd


def msg_by_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Total number of messages by year
    """
    result = df[['year', 'sender_name']] \
        .groupby('year') \
        .count() \
        .reset_index() \
        .rename(columns={'year': 'keys', 'sender_name': 'values'}) \
        .sort_values('keys')
    return result
