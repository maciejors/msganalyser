from datetime import date

import pandas as pd


def days_with_msg_count(df: pd.DataFrame) -> pd.DataFrame:
    """
    The ranking of chats based on the number of days with at least one message.
    """
    result = df[['chat_name', 'year', 'month', 'day']] \
        .drop_duplicates() \
        .groupby('chat_name') \
        .count() \
        .reset_index() \
        .rename(columns={'year': 'value'}) \
        .sort_values('value', ascending=False)
    return result[['chat_name', 'value']]


def longest_streaks(df: pd.DataFrame) -> pd.DataFrame:
    """
    The ranking of chats based on the longest streak of days with at least
    one message. Only chats with the longest streak of at least 2 are
    included. As a tie-breaker, the longest streak count is used.
    """
    days_with_messages = df[['chat_name']] \
        .assign(day=df['timestamp_ms'].map(
            lambda t: date.fromtimestamp(t / 1000))) \
        .drop_duplicates() \
        .sort_values('day', ascending=True)

    longest_streaks_dict = {'chat_name': [], 'value': [], 'count': []}

    for chat_name in days_with_messages['chat_name'].unique():
        chat_days = days_with_messages.loc[
                        days_with_messages['chat_name'] == chat_name].loc[:, 'day']
        diffs_series = chat_days \
            .diff() \
            .reset_index(drop=True) \
            .drop(0) \
            .map(lambda delta: delta.days)

        longest_streak = 1
        curr_streak = 1
        longest_streak_count = 1

        for diff in diffs_series:
            if diff == 1:
                curr_streak += 1
            else:
                if curr_streak > longest_streak:
                    longest_streak = curr_streak
                    longest_streak_count = 1
                elif curr_streak == longest_streak:
                    longest_streak_count += 1
                curr_streak = 1
        if curr_streak > longest_streak:
            longest_streak = curr_streak
            longest_streak_count = 1

        # streaks of 1 will be ignored here
        if longest_streak > 1:
            longest_streaks_dict['chat_name'].append(chat_name)
            longest_streaks_dict['value'].append(longest_streak)
            longest_streaks_dict['count'].append(longest_streak_count)

    result = pd.DataFrame(longest_streaks_dict) \
        .sort_values(by=['value', 'count'], ascending=False)
    return result
