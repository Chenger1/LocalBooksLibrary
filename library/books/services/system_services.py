import os

from common.system_data import transform_unix_time

from books.utils.subfolders_utils import get_folders


def check_books_folder_last_update() -> bool:
    """
        Check last book`s folder update time and compares it with saved in date.
        If it are not equal: return False. Else: return True

    :return: bool
    """
    folder = get_folders(is_top_folder=True)
    last_time_update = transform_unix_time(os.path.getmtime(folder.path))

    if last_time_update > folder.created:
        return True

    return False

