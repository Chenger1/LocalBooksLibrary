from typing import Union

from books.models import Folder, Book

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet


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


def get_books(book_id=None, all_books=False) -> Union[QuerySet[Book], Book, None]:
    try:
        if all_books:
            books = Book.objects.all()
        elif book_id:
            books = Book.objects.get(pk=book_id)
        else:
            return None
    except ObjectDoesNotExist:
        return None
    else:
        return books
