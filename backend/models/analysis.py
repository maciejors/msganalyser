from pydantic import BaseModel


class Overview(BaseModel):
    """
    Represents general overview statictics. All attributes are one-element
    lists.
    """
    total_msg_count: list[int]
    total_calls_count: list[int]
    total_calls_duration_s: list[int]
    total_media_count: list[int]
    favourite_chat: list[str]
    most_active_day: list[str]


class DatetimeActivityStat(BaseModel):
    """
    Represents one-dimenional statistics grouped by datetime or values
    dependent on datetime (e.g. year, month, day, hour).

    This is used for activity analysis where no chat name is needed.
    """
    datetime_key: list[str]
    value: list[int]
    

class DateChatStat(DatetimeActivityStat):
    """
    Represents one-dimenional statistics grouped by datetime or values
    dependent on datetime (e.g. year, month, day, hour).
    
    This is used for chat analysis where datetime is involved, where
    aside from values a chat name is needed.
    """
    chat_name: list[str]


class ChatStat(BaseModel):
    """
    Represents one-dimenional statistic grouped by a chat.

    This is used for chat analysis for chat rankings based on a value of
    a 1D statistic.
    """
    chat_name: list[str]
    value: list[int]


class ChatStreakStat(ChatStat):
    """
    Used to represent streak rankings, as they are a 2-dimensional stat.
    """
    count: list[int]
