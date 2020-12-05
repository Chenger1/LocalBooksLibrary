from typing import Union

from books.models import Folder

from django.core.exceptions import ObjectDoesNotExist


def get_folders(folder_id: int) -> Union[int, None]:
    try:
        folder = Folder.objects.get(pk=folder_id)
    except ObjectDoesNotExist:
        folder = None

    return folder
