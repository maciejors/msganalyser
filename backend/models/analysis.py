from pydantic import BaseModel


class DatetimeStat1D(BaseModel):
    """
    Represents one-dimenional statistics grouped by datetime or values
    dependent on datetime (e.g. year, month, day, hour)
    """
    keys: list[str | int]
    values: list[int]
