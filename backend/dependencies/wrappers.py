from typing import Callable, Any, TypeVar

import pandas as pd
from pydantic import BaseModel

from backend.dependencies.filters import Filters


T = TypeVar('T', bound=BaseModel)


def standard_functionality_wrapper(
        func: Callable[[pd.DataFrame], pd.DataFrame],
        df: pd.DataFrame,
        filters: Filters,
        out_model: Callable[[Any], T]) -> T:
    """
    Args:
        func: A functionality callable
        df: Messages data
        filters: Filters to apply to the input data
        out_model: A callable that outputs a desired data model

    Returns:
        Data ready to be sent to the client
    """
    # 1. apply filters to the data
    filtered_df = filters.apply(df)
    # 2. process the data using the selected functionality
    out_df = func(filtered_df)
    # 3. change the results type to a model
    data_dict = out_df.to_dict(orient='list')
    output = out_model(**data_dict)
    return output
