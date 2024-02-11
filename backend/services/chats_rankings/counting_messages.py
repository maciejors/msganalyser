import re

import pandas as pd


def top_msg_count(df: pd.DataFrame) -> pd.DataFrame:
    """
    The ranking of chats based on the total number of messages.
    """
    result = df.groupby('chat_name') \
        .count() \
        .rename(columns={'sender_name': 'value'}) \
        .reset_index() \
        .sort_values('value', ascending=False)
    return result[['chat_name', 'value']]


def top_media_count(df: pd.DataFrame) -> pd.DataFrame:
    """
    The ranking of chats based on the total number of media (photos, videos
    and files).
    """

    def extract_media_count(tag_set: str) -> int:
        photos_match = re.search(r'<@photos=(\d+)>', tag_set)
        videos_match = re.search(r'<@videos=(\d+)>', tag_set)
        files_match = re.search(r'<@files=(\d+)>', tag_set)
        media_count = 0
        if photos_match is not None:
            media_count += int(photos_match.group(1))
        if videos_match is not None:
            media_count += int(videos_match.group(1))
        if files_match is not None:
            media_count += int(files_match.group(1))
        return media_count

    msg_with_media = df[
        df['@tags'].str.contains('photos|videos|files')]
    media_counts_series = msg_with_media['@tags'].map(extract_media_count)
    result = msg_with_media \
        .assign(value=media_counts_series) \
        .groupby('chat_name') \
        .sum() \
        .reset_index() \
        .sort_values('value', ascending=False)
    return result[['chat_name', 'value']]
