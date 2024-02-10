from pydantic import BaseModel


class TwoDimensionalData(BaseModel):
    """
    Example:
        Data for a bar chart, with ``keys`` used as categories and ``values``
        denoting bars height
    """
    keys: list[str | int]
    values: list[int]
