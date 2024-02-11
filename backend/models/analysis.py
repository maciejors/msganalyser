from pydantic import BaseModel


class DatetimeActivityStat(BaseModel):
    """
    Represents one-dimenional statistics grouped by datetime or values
    dependent on datetime (e.g. year, month, day, hour).

    This is used for activity analysis where no chat name is needed.
    """
    key: list[str | int]
    value: list[int]
    

class DateChatStat(DatetimeActivityStat):
    """
    Represents one-dimenional statistics grouped by datetime or values
    dependent on datetime (e.g. year, month, day, hour).
    
    This is used for chat analysis where datetime is involved, where
    aside from values a chat name is needed.
    """
    chat_name: list[str]
