import pandas as pd


def msg_per_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Number of messages per year
    """
    result = df[['year', 'sender_name']] \
        .groupby('year') \
        .count() \
        .reset_index() \
        .rename(columns={'year': 'keys', 'sender_name': 'values'}) \
        .sort_values('keys')
    return result
