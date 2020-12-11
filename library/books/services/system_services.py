import json
import os

from django.conf import settings


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
