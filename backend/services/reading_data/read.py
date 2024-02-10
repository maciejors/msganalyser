import json
import os
import re
import shutil
import logging
from zipfile import ZipFile
from datetime import datetime

import numpy as np
import pandas as pd


_logger = logging.getLogger('services.reading_data')


def __extract_merged_inbox(fb_data_folder_path: str) -> str:
    """
    Data from Facebook can come split between different archives which can
    make it challenging to analyse.

    This function extracts message history from different FB data archives
    and merges that data into one single folder containing all message history.

    Args:
        fb_data_folder_path: A path to a directory containing archives
            downloaded from Facebook

    Returns:
        A path to a folder with extracted data
    """
    _logger.info('Preparing for data extraction...')

    # initial inspection of data - see how many zip files there are
    all_files = os.listdir(fb_data_folder_path)
    zip_files = [filename for filename in all_files if filename.endswith('.zip')]
    n_of_files = len(zip_files)
    if n_of_files == 0:
        raise FileNotFoundError('No facebook data found.')

    # a path where the contents extracted from the zipfiles will be stored
    extr_temp_dir = os.path.join(fb_data_folder_path,
                                 f'tmp-{np.random.randint(0, 100000)}')
    os.makedirs(extr_temp_dir)

    # this directory normally is deleted at the end of this function execution,
    # but in case something goes wrong, a readme will be left there informing
    # the user that this directory can be safely deleted
    with open(os.path.join(extr_temp_dir, 'README.txt'),
              'w', encoding='utf-8') as readme:
        readme.write('You can safely delete this directory (unless the '
                     'program is still running)')

    _logger.info('Done')

    # unzip data and place it in a temporary directory
    for i, filename in enumerate(zip_files):
        _logger.info(f'Extracting data (file {i+1}/{n_of_files})...')
        with ZipFile(os.path.join(fb_data_folder_path, filename), 'r') as fbzip:
            fbzip.extractall(os.path.join(extr_temp_dir, str(i)))
        _logger.info('Done')

    # merge the data
    _logger.info('Merging data...')

    output_path = os.path.join(fb_data_folder_path,
                               f'extracted-{np.random.randint(0, 100000)}')
    os.makedirs(output_path, exist_ok=False)

    # this directory normally will be deleted once the data is read by 
    # __read_extracted_data function,
    # but in case something goes wrong, a readme will be left there informing
    # the user that this directory can be safely deleted
    with open(os.path.join(output_path, 'README.txt'),
              'w', encoding='utf-8') as readme:
        readme.write('You can safely delete this directory (unless the '
                     'program is still running)')

    # this dict stores information on how many message_X.json files have
    # already been moved to the output directory for every chat
    # will be used when naming message_X.json files in the output
    # directory
    chat_msgfiles_counts = {}

    for i in range(n_of_files):
        # since Meta introduced e2e encrypted chats, the chat data is split between two folders
        inbox_path_legacy = os.path.join(
            extr_temp_dir, str(i), 'your_activity_across_facebook', 'messages', 'inbox'
        )
        inbox_path_e2ee = os.path.join(
            extr_temp_dir, str(i), 'your_activity_across_facebook', 'messages', 'e2ee_cutover'
        )
        for inbox_path in (inbox_path_legacy, inbox_path_e2ee):
            for chat_name in os.listdir(inbox_path):
                # add the chat name to the chat_msgfiles_counts dict
                # if it's not there yet and add an output folder for it
                if chat_name not in chat_msgfiles_counts.keys():
                    chat_msgfiles_counts[chat_name] = 0
                    os.makedirs(os.path.join(output_path, chat_name))

                # move all message_X.json files to the target directory
                for filename in os.listdir(os.path.join(inbox_path, chat_name)):
                    if re.match('message_\\d+\\.json', filename):
                        os.rename(
                            os.path.join(inbox_path, chat_name, filename),
                            os.path.join(output_path, chat_name,
                                         f'message_{chat_msgfiles_counts[chat_name]}.json'))
                        # increment so that every moved file has a unique name
                        chat_msgfiles_counts[chat_name] += 1

    _logger.info('Done')

    # remove the temporary directory
    shutil.rmtree(extr_temp_dir)
    return output_path


def __fix_fb_encoding(string: str) -> str:
    """
    Data from Facebook comes badly encoded.
    This function fixes the issue for a given string.

    Args:
        string: A string to recode
    
    Returns:
        Correctly recoded string

    See also:
        https://stackoverflow.com/questions/50008296/facebook-json-badly-encoded
    """
    return string.encode('latin1').decode('utf8')


def __read_single_message_json(path: str) -> pd.DataFrame:
    """
    Reads a single message_X.json file and stores selected message data
    in a data frame.

    Args:
        path: path to the message_X.json file
    
    Returns:
        A data frame containing the message history as well as the
        conversation title and its type
    """
    with open(path) as file:
        raw_data_full = json.load(file)
        conversation_name = __fix_fb_encoding(raw_data_full['title'])
        participants = raw_data_full['participants']
        raw_msg_data = raw_data_full['messages']

    # only sender name, content and timestamp are needed
    # the rest will be filtered out below

    # preallocating the list for the filtered message data
    relevant_msg_data = [{} for _ in range(len(raw_msg_data))]

    skipped_count = 0  # will be useful later to shorten the list defined above

    # indexing manually instead of using enumerate because
    # the value of i will sometimes not be incremented
    i = 0
    for message_data in raw_msg_data:
        # check if the message was unsent
        if message_data.get('is_unsent'):
            # if so, skip it
            skipped_count += 1
            continue

        # the message will be marked with special tags if it contains
        # a photo/gif/sticker etc.
        # (may be useful later when processing this data)
        # tag syntax: <@tag=[count]>
        # for example: <@photo=3> means that 3 photos were sent with that message
        # exception to that is a @call tag where instead of count, a call duration
        # (in seconds) is being stored as a value
        message_data['@tags'] = ''

        # check if the message contains a sticker
        if 'sticker' in message_data.keys():
            message_data['@tags'] += '<@sticker>'

        # check if the message is a call
        if 'call_duration' in message_data.keys():
            message_data['@tags'] += f'<@call={message_data["call_duration"]}>'

        # check if the message contains a gif/audio_file/video/photo
        media_tags = ['gifs', 'audio_files', 'videos', 'photos', 'files']
        for tag in media_tags:
            if tag in message_data.keys():
                message_data['@tags'] += f'<@{tag}={len(message_data[tag])}>'

        # if no tags were assigned and message has no content anyway,
        # it will be skipped
        if 'content' not in message_data.keys() and message_data['@tags'] == '':
            skipped_count += 1
            continue

        # if it has no content but contains some tags,
        # an empty string will be assigned to that key
        elif message_data['@tags'] != '':
            message_data['content'] = ''

        # fixing the encoding
        # see: https://stackoverflow.com/questions/50008296/facebook-json-badly-encoded
        message_data['sender_name'] = __fix_fb_encoding(message_data['sender_name'])
        message_data['content'] = __fix_fb_encoding(message_data['content'])

        # filtering keys
        relevant_keys = ['sender_name', 'timestamp_ms', 'content', '@tags']
        message_data = {key: message_data[key]
                        for key in relevant_keys}

        # add new message data to the list
        relevant_msg_data[i] = message_data
        i += 1

    # remove empty dictionaties from the end of the list
    # there are as many empty dictionaries as the number of skipped messages
    # during iteration
    # this check is necessary to avoid slicing with [:-0], as it clears the list
    if skipped_count > 0:
        relevant_msg_data = relevant_msg_data[:-skipped_count]

    df = pd.DataFrame(relevant_msg_data)
    df['conversation_name'] = conversation_name
    df['participants_count'] = len(participants)
    return df


def __read_all_messages_from_conversation(path: str) -> pd.DataFrame:
    """
    Reads all message_X.json files from a conversation and stores selected
    message data in a data frame.

    Args:
        path: path to a folder with the conversation data
    
    Returns:
        A data frame containing the message history as well as the
        conversation title and the number of participants
    """
    # get names of all message_X.json files
    message_json_files = [filename for filename in os.listdir(path)
                          if re.match('message_\\d+\\.json', filename)]

    # read every file individually and then join them
    all_data = [__read_single_message_json(os.path.join(path, filename))
                for filename in message_json_files]
    return pd.concat(all_data)


def __read_extracted_data(path: str) -> pd.DataFrame:
    """
    Reads the extracted messenger data and stores it in a data frame.
    Every data frame contains message_data with the message history,
    name and a number of participants.

    Args:
        path: Path to the folder with message history
    
    Returns:
        A data frame with the full messenger data

    Note: 
        the data must first be processed using the 
        extract_merged_inbox function
    """
    messenger_data = []

    # iterate over every conversation
    for conversation_folder_name in os.listdir(path):
        conversation_folder_path = os.path.join(path, conversation_folder_name)
        if not os.path.isdir(conversation_folder_path):
            # skip README.txt file
            continue
        chat_df = __read_all_messages_from_conversation(
            conversation_folder_path
        )
        messenger_data.append(chat_df)

    # remove the directory with extracted data
    shutil.rmtree(path)

    # reset index
    full_data = pd.concat(messenger_data)\
        .reset_index(drop=True)

    # add year/month/day/hour columns
    date_series = full_data['timestamp_ms'].map(lambda t: datetime.fromtimestamp(t / 1000))
    full_data['year'] = date_series.map(lambda d: d.year).astype(np.int16)
    full_data['month'] = date_series.map(lambda d: d.month).astype(np.int8)
    full_data['day'] = date_series.map(lambda d: d.day).astype(np.int8)
    full_data['hour'] = date_series.map(lambda d: d.hour).astype(np.int8)

    return full_data


def read_messenger_data(data_path: str, purge_contents=True):
    """
    Reads the entire messenger inbox data and stores it in a data frame.
    Every data frame contains message_data with the message history,
    name and a number of participants.

    Args:
        data_path: Path to the folder with zipped facebook data
        purge_contents: Whether or not to wipe messages contents 
            (reduces in-memory size)
    
    Returns:
        A data frame with the full messenger data
    """
    extracted_path = __extract_merged_inbox(data_path)
    full_data = __read_extracted_data(extracted_path)
    if purge_contents:
        full_data['content'] = ''
    return full_data


def infer_data_owner(full_data: pd.DataFrame) -> str:
    """
    Identifies the name of person who owns the data by peeking all chats with 
    two participants and at least two senders and checking which name appears 
    the most often.

    Args:
        full_data: full messages data
    """
    # step 1: filter data to chats with 2 participants
    chats_senders = full_data\
        [full_data['participants_count'] == 2]\
        [['conversation_name', 'sender_name']]\
        .drop_duplicates()
    # step 2: find the number of people who sent at least 1 message for each chat
    chats_sender_counts = chats_senders\
        .groupby('conversation_name')\
        .count()\
        .reset_index()\
        .rename(columns={'sender_name': 'conversation_sender_count'})
    # step 3: merge both data frames to enable filtering
    chats_senders = chats_senders\
        .merge(chats_sender_counts, on='conversation_name')
    # step 4: filter out chats with less than 2 senders,
    # count how many times in general each sender appears.
    senders_counts = chats_senders\
        [chats_senders['conversation_sender_count'] == 2]\
        .groupby('sender_name')\
        .count()\
        .reset_index()\
        .rename(columns={'conversation_name': 'count'})
    # step 5: argmax = data owner
    owner_name = senders_counts\
        .iloc[senders_counts['count'].idxmax()]\
        ['sender_name']
    return owner_name
