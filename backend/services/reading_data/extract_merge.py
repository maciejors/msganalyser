import os
import re
import shutil
from zipfile import ZipFile

import numpy as np


def extract_merged_inbox(fb_data_folder_path: str):
    """
    Data from Facebook can come split between different archives which can
    make it challenging to analyse.

    This function extracts message history from different FB data archives
    and merges that data into one single folder containing all message history.

    Args:
        fb_data_folder_path: A path to a directory containing archives
            downloaded from Facebook
    """
    print('Preparing for data extraction... ')

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

    print('done')

    # unzip data and place it in a temporary directory
    all_files = os.listdir(fb_data_folder_path)
    zip_files = [filename for filename in all_files if filename.endswith('.zip')]
    n_of_files = len(zip_files)
    for i, filename in enumerate(zip_files):
        print(f'Extracting data (file {i+1}/{n_of_files})... ')
        with ZipFile(os.path.join(fb_data_folder_path, filename), 'r') as fbzip:
            fbzip.extractall(os.path.join(extr_temp_dir, str(i)))
        print('done')

    # merge the data
    print('Merging data... ')

    output_path = os.path.join(fb_data_folder_path, 'extracted')
    os.makedirs(output_path, exist_ok=False)
    
    # this directory normally will be deleted once the data is read by another module,
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

    print('done')

    # remove the temporary directory
    shutil.rmtree(extr_temp_dir)
