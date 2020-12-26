from typing import Union

from books.models import Folder

from django.core.exceptions import ObjectDoesNotExist


def get_folders(folder_id: int = None, is_top_folder: bool = False, folder_name: str = None) -> Union[Folder, None]:
    try:
        if folder_id:
            folder = Folder.objects.get(pk=folder_id)
        elif is_top_folder:
            folder = Folder.objects.get(is_top_folder=True)
        elif folder_name:
            folder = Folder.objects.get(name=folder_name)
        else:
            return None
    except ObjectDoesNotExist:
        return None
    else:
        return folder
