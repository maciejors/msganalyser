from typing import Callable

import pandas as pd

from backend.dependencies.filters import StandardFilters
from backend.models.analysis import DatetimeStat1D


def standard_functionality_wrapper(
        func: Callable[[pd.DataFrame], pd.DataFrame],
        df: pd.DataFrame,
        filters: StandardFilters) -> DatetimeStat1D:
    """
    Args:
        func: A functionality callable
        df: Messages data
        filters: Filters to apply to the input data

    Returns:
        Data ready to be sent to the client
    """
    # 1. apply filters to the data
    filtered_df = filters.apply(df)
    # 2. process the data using the selected functionality
    out_df = func(filtered_df)
    # 3. change the results type
    data_dict = out_df.to_dict(orient='list')
    return DatetimeStat1D(**data_dict)
