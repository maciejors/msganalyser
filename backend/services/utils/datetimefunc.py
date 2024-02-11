from datetime import datetime


def get_sortable_day_str_from_timestamp(timestamp_ms: int) -> str:
    """
    e.g. 1640283981955 -> "2021/12/01" (1st December 2021)
    """
    date = datetime.fromtimestamp(timestamp_ms / 1000)
    return f'{date.year}/{str(date.month).zfill(2)}/{str(date.day).zfill(2)}'


def get_pretty_day_str_from_sortable(sortable_day_str: str) -> str:
    """
    e.g. "2021/12/01" -> "01/12/2021" (1st December 2021)
    """
    yyyy, mm, dd = sortable_day_str.split('/')
    return f'{dd}/{mm}/{yyyy}'


def get_sortable_month_str_from_timestamp(timestamp_ms: int) -> str:
    """
    e.g. 1640283981955 -> "2021/12" (December 2021)
    """
    date = datetime.fromtimestamp(timestamp_ms / 1000)
    return f'{date.year}/{str(date.month).zfill(2)}'


def get_pretty_month_str_from_sortable(sortable_day_str: str) -> str:
    """
    e.g. "2021/12" -> "12/2021" (December 2021)
    """
    yyyy, mm = sortable_day_str.split('/')
    return f'{mm}/{yyyy}'
