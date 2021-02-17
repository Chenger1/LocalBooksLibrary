from datetime import datetime
import pytz
import shutil
import os

utc = pytz.UTC


def transform_unix_time(unix_time: float) -> datetime:
    """
    Transform unix type time into common
    :param unix_time: usual unix format time
    :return: datetime
    """
    return transform_to_utc(datetime.utcfromtimestamp(unix_time))


def transform_to_utc(naive_datetime: datetime) -> datetime:
    return naive_datetime.replace(tzinfo=utc)


def move_file_to_folder(file_path: str, folder_path: str) -> str:
    return shutil.move(file_path, folder_path)


def create_folder_in_system(file_path: str):
    os.mkdir(file_path)
