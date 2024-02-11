from pydantic import BaseModel


class DatetimeActivityStat(BaseModel):
    """
    Represents one-dimenional statistics grouped by datetime or values
    dependent on datetime (e.g. year, month, day, hour).

    This is used for activity analysis where no chat name is needed.
    """
    keys: list[str | int]
    values: list[int]
    

class DatetimeChatStat(DatetimeActivityStat):
    """
    Represents one-dimenional statistics grouped by datetime or values
    dependent on datetime (e.g. year, month, day, hour).
    
    This is used for chat analysis where datetime is involved, where
    aside from values a chat name is needed.
    """
    chat_names: list[str]
