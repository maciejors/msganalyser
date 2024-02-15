import logging
from datetime import datetime

import pandas as pd


_logger = logging.getLogger('services.loading_data')


def write_compact(df: pd.DataFrame, data_path: str) -> str:
    """
    Writes messenger data back with no files, making it way more compact and faster
    to load back. Returns the location where the file was saved.
    """
    _logger.info('Writing compacted data...')
    save_path = f'{data_path}/compacted-data_{datetime.now()}.compact.csv'
    df.to_csv(save_path)
    _logger.info(f'Done. Saved to {save_path}.')
    return save_path
