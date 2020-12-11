import json
import os

from django.conf import settings

from common.system_data import transform_unix_time


def init_system_data_file() -> str:
    """
    system_data file contains information about book`s folder

        Firstly check if file exists, if not: creates it
        :returns folder`s path
    """

    path = f'{settings.BASE_DIR}\\system_data.json'
    if not os.path.isfile(path):
        with open(path, 'w', encoding='utf-8') as file:
            json.dump([], file)

    return path


def write_data_to_file(data: dict, file: str):
    with open(file, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def get_data_from_file(file: str) -> dict:
    with open(file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def check_books_folder_last_update(file_path: str) -> bool:
    """
        Check last book`s folder update time and compares it with saved in json data.
        If it are not equal: return False. Else: return True

    :param file_path:
    :return: bool
    """
    info = get_data_from_file(file_path)

    try:
        last_time_update = transform_unix_time(os.path.getmtime(info['folder_path']), True)

        if last_time_update != info['last_time_update']:
            return False
        return True
    except KeyError:
        return False
