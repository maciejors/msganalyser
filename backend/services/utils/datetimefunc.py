from datetime import datetime


def get_sortable_day_str_from_timestamp(timestamp_ms: int) -> str:
    """
    e.g. 1640283981955 -> "2021/12/01" (1st December 2021)
    """
    date = datetime.fromtimestamp(timestamp_ms / 1000)
    return f'{date.year}/{str(date.month).zfill(2)}/{str(date.day).zfill(2)}'


def get_pretty_day_str_from_sortable(sortable_day_str: str) -> str:
    """
    e.g. "2021/12/01" -> "01/12" (1st December)
    """
    mm, dd = sortable_day_str[5:].split('/')
    return f'{dd}/{mm}'


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


def get_readable_time(seconds: int) -> str:
    """
    Turns something like this: 3731 (seconds)

    Into this: "1h 2m 11s"
    """
    hrs = seconds // 3600
    mins = (seconds % 3600) // 60
    secs = seconds % 60

    result = ''
    if hrs != 0:
        result += f'{hrs}h '
    if mins != 0:
        result += f'{mins}m '
    result += f'{secs}s'
    return result
