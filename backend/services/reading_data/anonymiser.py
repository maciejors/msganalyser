import json
import random
import itertools
import logging

import pandas as pd


_logger = logging.getLogger('services.reading_data')

PATH_TO_SUBSTITUTE_NAMES = './backend/static/substitute_names.json'


def __purge_contents(df: pd.DataFrame) -> pd.DataFrame:
    df['content'] = ''
    return df


def __replace_names(df: pd.DataFrame) -> pd.DataFrame:
    # read substitute names
    with open(PATH_TO_SUBSTITUTE_NAMES) as file:
        substitute_names = json.load(file)

    # find all original names to replace
    sender_names_original = set()
    sender_names_original.update(df['sender_name'].unique())
    # this is for chats with only one sender:
    sender_names_original.update(df.loc[df['participants_count'] <= 2, 'chat_name'].unique())
    group_names_original = set(df.loc[df['participants_count'] > 2, 'chat_name'].unique())

    # generate all possible combinations of substitute names
    sub_names_idx = list(range(len(substitute_names['senders']['names'])))
    sub_surnames_idx = list(range(len(substitute_names['senders']['surnames'])))
    sub_group_adjectives_idx = list(range(len(substitute_names['groups']['part1'])))
    sub_group_nouns_idx = list(range(len(substitute_names['groups']['part2'])))

    sub_sender_names_idx_combinations = list(itertools.product(sub_names_idx, sub_surnames_idx))
    sub_group_names_idx_combinations = list(itertools.product(sub_group_adjectives_idx, sub_group_nouns_idx))
    random.shuffle(sub_sender_names_idx_combinations)
    random.shuffle(sub_group_names_idx_combinations)

    # replace original sender names with synthetic names
    for sender_name_original, sender_name_new_idx in zip(sender_names_original,
                                                         sub_sender_names_idx_combinations):
        new_name = substitute_names['senders']['names'][sender_name_new_idx[0]]
        new_surname = substitute_names['senders']['surnames'][sender_name_new_idx[1]]
        df.loc[df['sender_name'] == sender_name_original, 'sender_name'] = f'{new_name} {new_surname}'
        df.loc[df['chat_name'] == sender_name_original, 'chat_name'] = f'{new_name} {new_surname}'

    # replace original group names with synthetic names
    for group_name_original, group_name_new_idx in zip(group_names_original,
                                                       sub_group_names_idx_combinations):
        new_name_adjective = substitute_names['groups']['part1'][group_name_new_idx[0]]
        new_name_noun = substitute_names['groups']['part2'][group_name_new_idx[1]]
        df.loc[df['chat_name'] == group_name_original, 'chat_name'] = \
            f'The {new_name_adjective} {new_name_noun}'
    return df


def anonymise_data(full_data: pd.DataFrame, purge_contents: bool, replace_names: bool) -> pd.DataFrame:
    """
    Args:
        full_data:
        purge_contents: Whether or not to wipe messages contents
            (reduces in-memory size)
        replace_names: Whether or not to anonymise all chat names
            and sender names

    Note:
        All operations are done in-place, i.e. affecting the original data frame
    """
    if purge_contents:
        _logger.info('Purging messages contents...')
        full_data = __purge_contents(full_data)
        _logger.info('Done')
    if replace_names:
        _logger.info('Anonymising sender and chat names...')
        full_data = __replace_names(full_data)
        _logger.info('Done')
    return full_data
