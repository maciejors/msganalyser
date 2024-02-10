from typing import Literal, Annotated

import pandas as pd
from fastapi import Depends


class StandardFilters:
    __slots__ = ['timestamp_ms_from', 'timestamp_ms_to', 'chat_type', 'message_type']

    def __init__(self,
                 timestamp_ms_from: int = -1,
                 timestamp_ms_to: int = -1,
                 chat_type: Literal['all', 'group', 'private'] = 'all',
                 message_type: Literal['all', 'sent', 'received'] = 'all'):
        self.timestamp_ms_from = timestamp_ms_from
        self.timestamp_ms_to = timestamp_ms_to
        self.chat_type = chat_type
        self.message_type = message_type

    def apply(self, df: pd.DataFrame) -> pd.DataFrame:
        if self.timestamp_ms_from != -1:
            df = df[df['timestamp_ms'] >= self.timestamp_ms_from]
        if self.timestamp_ms_to != -1:
            df = df[df['timestamp_ms'] <= self.timestamp_ms_to]

        if self.chat_type == 'group':
            df = df[df['participants_count'] > 2]
        elif self.chat_type == 'private':
            df = df[df['participants_count'] <= 2]

        if self.message_type == 'sent':
            df = df[df['is_owner']]
        elif self.chat_type == 'private':
            df = df[~df['is_owner']]

        return df


StandardFiltersAnnotated = Annotated[StandardFilters, Depends(StandardFilters)]
